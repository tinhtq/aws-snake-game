import pygame

def create_s3_icon(size):
    """Create an S3 icon surface"""
    surface = pygame.Surface((size, size), pygame.SRCALPHA)
    
    # S3 green color
    s3_color = (40, 167, 69)
    
    # Draw S3 icon (simplified AWS S3 bucket)
    # Draw bucket shape
    bucket_rect = pygame.Rect(2, size//4, size-4, size*3//4-2)
    pygame.draw.rect(surface, s3_color, bucket_rect, border_radius=3)
    
    # Draw bucket top
    top_rect = pygame.Rect(4, 2, size-8, size//4)
    pygame.draw.rect(surface, s3_color, top_rect)
    pygame.draw.ellipse(surface, s3_color, top_rect)
    
    # Add "S3" text-like markings
    pygame.draw.line(surface, (255, 255, 255), (size//3, size//2), (size*2//3, size//2), 2)
    pygame.draw.line(surface, (255, 255, 255), (size//3, size//2), (size//3, size*2//3), 2)
    pygame.draw.line(surface, (255, 255, 255), (size//3, size*2//3), (size*2//3, size*2//3), 2)
    pygame.draw.line(surface, (255, 255, 255), (size*2//3, size//2), (size*2//3, size*2//3), 2)
    
    return surface
