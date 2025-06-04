import pygame

def create_lambda_icon(size):
    """Create a Lambda icon surface"""
    surface = pygame.Surface((size, size), pygame.SRCALPHA)
    
    # Lambda orange color
    lambda_color = (255, 215, 0)
    
    # Draw Lambda icon (simplified AWS Lambda logo)
    # Draw square background
    rect = pygame.Rect(2, 2, size-4, size-4)
    pygame.draw.rect(surface, lambda_color, rect, border_radius=3)
    
    # Draw lambda symbol (λ)
    # Left diagonal line
    pygame.draw.line(surface, (0, 0, 0), (size//3, size//3), (size//2, size*2//3), 2)
    # Right diagonal line
    pygame.draw.line(surface, (0, 0, 0), (size//2, size*2//3), (size*2//3, size//3), 2)
    
    return surface
