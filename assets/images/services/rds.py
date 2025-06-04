import pygame

def create_rds_icon(size):
    """Create an RDS icon surface"""
    surface = pygame.Surface((size, size), pygame.SRCALPHA)
    
    # RDS blue color
    rds_color = (0, 123, 255)
    
    # Draw RDS icon (simplified AWS RDS logo)
    # Draw cylinder shape for database
    rect = pygame.Rect(2, size//4, size-4, size//2)
    pygame.draw.rect(surface, rds_color, rect)
    
    # Draw top ellipse
    ellipse_rect = pygame.Rect(2, 2, size-4, size//3)
    pygame.draw.ellipse(surface, rds_color, ellipse_rect)
    
    # Draw bottom ellipse
    ellipse_rect = pygame.Rect(2, size*2//3, size-4, size//3)
    pygame.draw.ellipse(surface, rds_color, ellipse_rect)
    
    # Add some details
    pygame.draw.line(surface, (255, 255, 255), (size//4, size//2), (size*3//4, size//2), 1)
    
    return surface
