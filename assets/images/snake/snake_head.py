import pygame

def create_snake_head(size, direction):
    """Create a snake head surface with AWS logo styling"""
    surface = pygame.Surface((size, size), pygame.SRCALPHA)
    
    # AWS blue color
    aws_blue = (0, 153, 255)
    
    # Draw head
    pygame.draw.rect(surface, aws_blue, (0, 0, size, size), border_radius=3)
    
    # Add AWS smile-like curve
    if direction == (0, -1):  # Up
        pygame.draw.arc(surface, (255, 255, 255), (size//4, size//2, size//2, size//2), 3.14, 0, 2)
        # Eyes
        pygame.draw.circle(surface, (255, 255, 255), (size//3, size//3), 2)
        pygame.draw.circle(surface, (255, 255, 255), (size*2//3, size//3), 2)
    elif direction == (0, 1):  # Down
        pygame.draw.arc(surface, (255, 255, 255), (size//4, 0, size//2, size//2), 0, 3.14, 2)
        # Eyes
        pygame.draw.circle(surface, (255, 255, 255), (size//3, size*2//3), 2)
        pygame.draw.circle(surface, (255, 255, 255), (size*2//3, size*2//3), 2)
    elif direction == (-1, 0):  # Left
        pygame.draw.arc(surface, (255, 255, 255), (size//2, size//4, size//2, size//2), 1.5*3.14, 0.5*3.14, 2)
        # Eyes
        pygame.draw.circle(surface, (255, 255, 255), (size//3, size//3), 2)
        pygame.draw.circle(surface, (255, 255, 255), (size//3, size*2//3), 2)
    else:  # Right
        pygame.draw.arc(surface, (255, 255, 255), (0, size//4, size//2, size//2), 0.5*3.14, 1.5*3.14, 2)
        # Eyes
        pygame.draw.circle(surface, (255, 255, 255), (size*2//3, size//3), 2)
        pygame.draw.circle(surface, (255, 255, 255), (size*2//3, size*2//3), 2)
    
    return surface
