import pygame

def create_ec2_icon(size):
    """Create an EC2 icon surface"""
    surface = pygame.Surface((size, size), pygame.SRCALPHA)
    
    # EC2 orange color
    ec2_color = (255, 153, 0)
    
    # Draw EC2 icon (simplified AWS EC2 logo)
    rect = pygame.Rect(2, 2, size-4, size-4)
    pygame.draw.rect(surface, ec2_color, rect, border_radius=3)
    
    # Add some details to make it look like EC2 icon
    pygame.draw.line(surface, (255, 255, 255), (size//4, size//3), (size*3//4, size//3), 2)
    pygame.draw.line(surface, (255, 255, 255), (size//4, size//2), (size*3//4, size//2), 2)
    pygame.draw.line(surface, (255, 255, 255), (size//4, size*2//3), (size*3//4, size*2//3), 2)
    
    return surface
