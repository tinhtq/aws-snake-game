import pygame

def create_snake_body(size, index):
    """Create a snake body segment with AWS styling"""
    surface = pygame.Surface((size, size), pygame.SRCALPHA)
    
    # AWS blue color with gradient based on segment index
    color_intensity = max(50, 255 - (index * 10))
    aws_blue = (0, 102, color_intensity)
    
    # Draw body segment
    pygame.draw.rect(surface, aws_blue, (0, 0, size, size), border_radius=3)
    
    # Add AWS logo-like detail
    if index % 3 == 0:
        # Add AWS-like arrow
        pygame.draw.line(surface, (255, 255, 255), (size//4, size//2), (size//2, size//4), 1)
        pygame.draw.line(surface, (255, 255, 255), (size//2, size//4), (size*3//4, size//2), 1)
    elif index % 3 == 1:
        # Add AWS-like dot
        pygame.draw.circle(surface, (255, 255, 255), (size//2, size//2), 2)
    else:
        # Add AWS-like line
        pygame.draw.line(surface, (255, 255, 255), (size//4, size//2), (size*3//4, size//2), 1)
    
    return surface
