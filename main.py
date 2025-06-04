import pygame
import random
import sys
import time
from aws_services import AWSService, PowerUp, AWSServiceType, PowerUpType
from assets.images.snake.snake_head import create_snake_head
from assets.images.snake.snake_body import create_snake_body

# Initialize pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE
FPS = 60

# Colors (AWS Theme)
AWS_DARK = (35, 47, 62)  # #232F3E - AWS console dark theme
AWS_ORANGE = (255, 153, 0)  # #FF9900 - AWS orange
WHITE = (255, 255, 255)
BLUE = (0, 102, 255)  # For snake body
LIGHT_BLUE = (51, 153, 255)  # For snake gradient

# Game states
MENU = 0
PLAYING = 1
GAME_OVER = 2
INSTRUCTIONS = 3
SERVICE_INFO = 4  # New state for service information popup

class Snake:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.length = 3
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        self.score = 0
        self.grow_to = 3  # Initial snake length
        
        # Power-up effects
        self.speed_boost = False
        self.speed_boost_end = 0
        self.invulnerable = False
        self.invulnerable_end = 0
        self.slow_mode = False
        self.slow_mode_end = 0
        self.extra_life = False
        
    def get_head_position(self):
        return self.positions[0]
        
    def update(self, current_time):
        # Update power-up timers
        if self.speed_boost and current_time > self.speed_boost_end:
            self.speed_boost = False
            
        if self.invulnerable and current_time > self.invulnerable_end:
            self.invulnerable = False
            
        if self.slow_mode and current_time > self.slow_mode_end:
            self.slow_mode = False
        
        head = self.get_head_position()
        x, y = self.direction
        new_position = ((head[0] + x) % GRID_WIDTH, (head[1] + y) % GRID_HEIGHT)
        
        # Check for collision with self
        if new_position in self.positions[1:]:
            if self.invulnerable:
                # Skip collision if invulnerable
                pass
            elif self.extra_life:
                # Use extra life
                self.extra_life = False
                return True
            else:
                return False  # Game over
            
        self.positions.insert(0, new_position)
        
        # Grow the snake if needed
        if len(self.positions) > self.grow_to:
            self.positions.pop()
            
        return True  # Game continues
        
    def render(self, surface):
        # Render head with AWS styling
        head_pos = self.positions[0]
        head_surface = create_snake_head(GRID_SIZE, self.direction)
        surface.blit(head_surface, (head_pos[0] * GRID_SIZE, head_pos[1] * GRID_SIZE))
        
        # Render body segments with AWS styling
        for i, p in enumerate(self.positions[1:], 1):
            body_surface = create_snake_body(GRID_SIZE, i)
            
            # Apply power-up visual effects
            if self.invulnerable:
                # Add red tint for invulnerability
                body_surface.fill((255, 0, 0, 50), special_flags=pygame.BLEND_RGBA_ADD)
            elif self.speed_boost:
                # Add purple tint for speed boost
                body_surface.fill((100, 0, 100, 50), special_flags=pygame.BLEND_RGBA_ADD)
            elif self.slow_mode:
                # Add green tint for slow mode
                body_surface.fill((0, 100, 0, 50), special_flags=pygame.BLEND_RGBA_ADD)
            
            surface.blit(body_surface, (p[0] * GRID_SIZE, p[1] * GRID_SIZE))
            
    def change_direction(self, direction):
        # Prevent 180-degree turns
        if (direction[0] * -1, direction[1] * -1) == self.direction:
            return
        self.direction = direction
        
    def apply_powerup(self, powerup_type, duration, current_time):
        if powerup_type == PowerUpType.CLOUDFRONT:
            # Speed boost
            self.speed_boost = True
            self.speed_boost_end = current_time + duration
            
        elif powerup_type == PowerUpType.WAF:
            # Invulnerability
            self.invulnerable = True
            self.invulnerable_end = current_time + duration
            
        elif powerup_type == PowerUpType.AUTO_SCALING:
            # Slow mode
            self.slow_mode = True
            self.slow_mode_end = current_time + duration
            
        elif powerup_type == PowerUpType.MULTI_AZ:
            # Extra life
            self.extra_life = True

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('AWS Snake Game')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 24)
        self.big_font = pygame.font.SysFont('Arial', 48)
        self.small_font = pygame.font.SysFont('Arial', 16)
        
        self.snake = Snake()
        self.aws_service = AWSService(GRID_SIZE)
        self.powerup = PowerUp(GRID_SIZE)
        self.powerup.active = False
        
        self.state = MENU
        self.high_score = 0
        self.last_update_time = 0
        self.update_delay = 0.1  # Base speed (seconds per move)
        self.powerup_spawn_timer = 0
        self.active_powerups = []  # List of (type, end_time) tuples
        
        # Track discovered services for first-time info popups
        self.discovered_services = set()
        self.current_service_info = None
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if self.state == MENU:
                    if event.key == pygame.K_SPACE:
                        self.state = PLAYING
                    elif event.key == pygame.K_i:
                        self.state = INSTRUCTIONS
                        
                elif self.state == INSTRUCTIONS:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                        self.state = MENU
                        
                elif self.state == PLAYING:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction((0, -1))
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction((0, 1))
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction((-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction((1, 0))
                    elif event.key == pygame.K_ESCAPE:
                        self.state = MENU
                        
                elif self.state == SERVICE_INFO:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                        self.state = PLAYING
                        
                elif self.state == GAME_OVER:
                    if event.key == pygame.K_SPACE:
                        self.snake.reset()
                        self.aws_service.randomize_position(GRID_WIDTH, GRID_HEIGHT)
                        self.powerup.active = False
                        self.state = PLAYING
                    elif event.key == pygame.K_ESCAPE:
                        self.state = MENU
                        
    def update(self):
        current_time = time.time()
        
        if self.state == PLAYING:
            # Determine movement speed based on power-ups
            move_delay = self.update_delay
            if self.snake.speed_boost:
                move_delay *= 0.5  # Twice as fast
            elif self.snake.slow_mode:
                move_delay *= 2.0  # Half as fast
                
            # Update snake position based on speed
            if current_time - self.last_update_time > move_delay:
                self.last_update_time = current_time
                
                # Update snake
                if not self.snake.update(current_time):
                    self.state = GAME_OVER
                    if self.snake.score > self.high_score:
                        self.high_score = self.snake.score
                    
            # Check for AWS service collision
            if self.snake.get_head_position() == self.aws_service.position:
                self.snake.grow_to += 1
                self.snake.score += self.aws_service.points
                
                # Check if this is the first time collecting this service
                if self.aws_service.service_type not in self.discovered_services:
                    self.discovered_services.add(self.aws_service.service_type)
                    self.current_service_info = self.aws_service.service_type
                    self.state = SERVICE_INFO
                
                # Generate a new AWS service
                self.aws_service = AWSService(GRID_SIZE)
                self.aws_service.randomize_position(GRID_WIDTH, GRID_HEIGHT)
                
                # Make sure service doesn't appear on snake
                while self.aws_service.position in self.snake.positions:
                    self.aws_service.randomize_position(GRID_WIDTH, GRID_HEIGHT)
                    
            # Check for power-up collision
            if self.powerup.active and self.snake.get_head_position() == self.powerup.position:
                powerup_type, duration = self.powerup.activate()
                self.snake.apply_powerup(powerup_type, duration, current_time)
                self.active_powerups.append((powerup_type, current_time + duration))
                
            # Spawn power-ups occasionally
            if not self.powerup.active and current_time > self.powerup_spawn_timer:
                # Random chance to spawn a power-up
                if random.random() < 0.01:  # 1% chance per frame when eligible
                    self.powerup = PowerUp(GRID_SIZE)
                    self.powerup.randomize_position(GRID_WIDTH, GRID_HEIGHT)
                    
                    # Make sure power-up doesn't appear on snake or service
                    while self.powerup.position in self.snake.positions or self.powerup.position == self.aws_service.position:
                        self.powerup.randomize_position(GRID_WIDTH, GRID_HEIGHT)
                        
                    self.powerup_spawn_timer = current_time + random.uniform(5, 15)  # Next spawn opportunity
                    
            # Update active power-ups list
            self.active_powerups = [(t, e) for t, e in self.active_powerups if e > current_time]
                    
    def render(self):
        self.screen.fill(AWS_DARK)
        
        if self.state == MENU:
            self.render_menu()
        elif self.state == INSTRUCTIONS:
            self.render_instructions()
        elif self.state == PLAYING:
            self.render_game()
        elif self.state == SERVICE_INFO:
            self.render_game()  # Render game in background
            self.render_service_info()  # Overlay service info
        elif self.state == GAME_OVER:
            self.render_game()
            self.render_game_over()
            
        pygame.display.update()
        
    def render_menu(self):
        title = self.big_font.render('AWS Snake Game', True, AWS_ORANGE)
        start_text = self.font.render('Press SPACE to Start', True, WHITE)
        instructions_text = self.font.render('Press I for Instructions', True, WHITE)
        
        self.screen.blit(title, (WINDOW_WIDTH // 2 - title.get_width() // 2, WINDOW_HEIGHT // 3))
        self.screen.blit(start_text, (WINDOW_WIDTH // 2 - start_text.get_width() // 2, WINDOW_HEIGHT // 2))
        self.screen.blit(instructions_text, (WINDOW_WIDTH // 2 - instructions_text.get_width() // 2, WINDOW_HEIGHT // 2 + 40))
        
        # Draw high score
        if self.high_score > 0:
            high_score_text = self.font.render(f'High Score: {self.high_score}', True, AWS_ORANGE)
            self.screen.blit(high_score_text, (WINDOW_WIDTH // 2 - high_score_text.get_width() // 2, WINDOW_HEIGHT // 2 + 100))
            
    def render_instructions(self):
        title = self.big_font.render('Instructions', True, AWS_ORANGE)
        self.screen.blit(title, (WINDOW_WIDTH // 2 - title.get_width() // 2, 50))
        
        instructions = [
            "Use arrow keys to control the snake",
            "Collect AWS services to grow and score points:",
            "  - EC2 (Orange Rectangle): 10 points",
            "  - S3 (Green Circle): 15 points",
            "  - Lambda (Yellow Triangle): 20 points",
            "  - RDS (Blue Diamond): 25 points",
            "",
            "Power-ups:",
            "  - CloudFront (Purple Star): Speed boost for 5 seconds",
            "  - WAF Shield (Red Hexagon): Wall invulnerability for 3 seconds",
            "  - Auto Scaling (Green Plus): Slows snake for 7 seconds",
            "  - Multi-AZ (Blue Cross): Extra life (hit wall once without dying)",
            "",
            "First-time service collection shows information about AWS services",
            "",
            "Press ESC or SPACE to return to menu"
        ]
        
        y_offset = 120
        for line in instructions:
            text = self.font.render(line, True, WHITE)
            self.screen.blit(text, (50, y_offset))
            y_offset += 30
            
    def render_service_info(self):
        # Create semi-transparent overlay
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        # Create popup box
        popup_width = 600
        popup_height = 300
        popup_x = (WINDOW_WIDTH - popup_width) // 2
        popup_y = (WINDOW_HEIGHT - popup_height) // 2
        
        # Draw popup background
        popup_rect = pygame.Rect(popup_x, popup_y, popup_width, popup_height)
        pygame.draw.rect(self.screen, AWS_DARK, popup_rect)
        pygame.draw.rect(self.screen, AWS_ORANGE, popup_rect, 3)
        
        # Draw service name
        service_name = AWSServiceType.get_name(self.current_service_info)
        name_text = self.big_font.render(f"AWS {service_name}", True, AWS_ORANGE)
        self.screen.blit(name_text, (popup_x + 20, popup_y + 20))
        
        # Draw service description
        description = AWSServiceType.get_description(self.current_service_info)
        
        # Word wrap the description
        words = description.split()
        lines = []
        line = ""
        for word in words:
            test_line = line + word + " "
            # Check if adding this word would exceed the width
            if self.font.size(test_line)[0] < popup_width - 40:
                line = test_line
            else:
                lines.append(line)
                line = word + " "
        lines.append(line)  # Add the last line
        
        # Draw the wrapped text
        y_offset = popup_y + 80
        for line in lines:
            text = self.font.render(line, True, WHITE)
            self.screen.blit(text, (popup_x + 20, y_offset))
            y_offset += 30
        
        # Draw continue prompt
        continue_text = self.font.render("Press SPACE to continue", True, WHITE)
        self.screen.blit(continue_text, (popup_x + (popup_width - continue_text.get_width()) // 2, 
                                        popup_y + popup_height - 50))
        
    def render_game(self):
        # Draw grid (optional)
        # for x in range(0, WINDOW_WIDTH, GRID_SIZE):
        #     pygame.draw.line(self.screen, (40, 40, 40), (x, 0), (x, WINDOW_HEIGHT))
        # for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
        #     pygame.draw.line(self.screen, (40, 40, 40), (0, y), (WINDOW_WIDTH, y))
            
        # Draw AWS service and snake
        self.aws_service.render(self.screen)
        if self.powerup.active:
            self.powerup.render(self.screen)
        self.snake.render(self.screen)
        
        # Draw score
        score_text = self.font.render(f'Score: {self.snake.score}', True, AWS_ORANGE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw active power-ups
        current_time = time.time()
        y_offset = 40
        for powerup_type, end_time in self.active_powerups:
            remaining = max(0, end_time - current_time)
            name = PowerUpType.get_name(powerup_type)
            color = PowerUpType.get_color(powerup_type)
            
            if remaining > 0:
                powerup_text = self.small_font.render(f'{name}: {remaining:.1f}s', True, color)
                self.screen.blit(powerup_text, (10, y_offset))
                y_offset += 20
                
        # Legend removed to prevent blocking the snake
        
    def render_legend(self):
        legend_items = [
            (AWSServiceType.EC2, f"EC2: {AWSServiceType.get_points(AWSServiceType.EC2)}pts"),
            (AWSServiceType.S3, f"S3: {AWSServiceType.get_points(AWSServiceType.S3)}pts"),
            (AWSServiceType.LAMBDA, f"Lambda: {AWSServiceType.get_points(AWSServiceType.LAMBDA)}pts"),
            (AWSServiceType.RDS, f"RDS: {AWSServiceType.get_points(AWSServiceType.RDS)}pts")
        ]
        
        legend_x = WINDOW_WIDTH - 150
        legend_y = 10
        
        legend_bg = pygame.Rect(legend_x - 10, legend_y - 5, 150, 110)
        pygame.draw.rect(self.screen, (0, 0, 0, 128), legend_bg)
        pygame.draw.rect(self.screen, AWS_ORANGE, legend_bg, 1)
        
        legend_title = self.small_font.render("AWS Services", True, AWS_ORANGE)
        self.screen.blit(legend_title, (legend_x, legend_y))
        
        y_offset = legend_y + 25
        for service_type, label in legend_items:
            # Create a mini icon for the legend
            icon = AWSServiceType.get_icon(service_type, 15)
            self.screen.blit(icon, (legend_x, y_offset))
            
            # Draw label
            text = self.small_font.render(label, True, WHITE)
            self.screen.blit(text, (legend_x + 25, y_offset))
            
            y_offset += 20
        
    def render_game_over(self):
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        game_over_text = self.big_font.render('GAME OVER', True, AWS_ORANGE)
        score_text = self.font.render(f'Score: {self.snake.score}', True, WHITE)
        high_score_text = self.font.render(f'High Score: {self.high_score}', True, WHITE)
        restart_text = self.font.render('Press SPACE to Restart', True, WHITE)
        menu_text = self.font.render('Press ESC for Menu', True, WHITE)
        
        self.screen.blit(game_over_text, (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, WINDOW_HEIGHT // 3))
        self.screen.blit(score_text, (WINDOW_WIDTH // 2 - score_text.get_width() // 2, WINDOW_HEIGHT // 2))
        self.screen.blit(high_score_text, (WINDOW_WIDTH // 2 - high_score_text.get_width() // 2, WINDOW_HEIGHT // 2 + 30))
        self.screen.blit(restart_text, (WINDOW_WIDTH // 2 - restart_text.get_width() // 2, WINDOW_HEIGHT // 2 + 80))
        self.screen.blit(menu_text, (WINDOW_WIDTH // 2 - menu_text.get_width() // 2, WINDOW_HEIGHT // 2 + 110))
        
    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()
