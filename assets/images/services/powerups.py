import pygame

def create_cloudfront_icon(size):
    """Create a CloudFront icon surface"""
    surface = pygame.Surface((size, size), pygame.SRCALPHA)
    
    # CloudFront purple color
    cf_color = (148, 0, 211)
    
    # Draw CloudFront icon (simplified)
    # Draw circle
    pygame.draw.circle(surface, cf_color, (size//2, size//2), size//2-2)
    
    # Draw globe-like lines
    pygame.draw.line(surface, (255, 255, 255), (2, size//2), (size-2, size//2), 1)
    pygame.draw.line(surface, (255, 255, 255), (size//2, 2), (size//2, size-2), 1)
    pygame.draw.arc(surface, (255, 255, 255), (2, 2, size-4, size-4), 0, 3.14, 1)
    pygame.draw.arc(surface, (255, 255, 255), (2, 2, size-4, size-4), 3.14, 6.28, 1)
    
    return surface

def create_waf_icon(size):
    """Create a WAF icon surface"""
    surface = pygame.Surface((size, size), pygame.SRCALPHA)
    
    # WAF red color
    waf_color = (255, 0, 0)
    
    # Draw WAF icon (simplified shield)
    # Shield shape
    points = [
        (size//2, 2),
        (size-2, size//3),
        (size-2, size*2//3),
        (size//2, size-2),
        (2, size*2//3),
        (2, size//3)
    ]
    pygame.draw.polygon(surface, waf_color, points)
    
    # Add shield details
    pygame.draw.line(surface, (255, 255, 255), (size//2, size//4), (size//2, size*3//4), 2)
    pygame.draw.line(surface, (255, 255, 255), (size//3, size//2), (size*2//3, size//2), 2)
    
    return surface

def create_autoscaling_icon(size):
    """Create an Auto Scaling icon surface"""
    surface = pygame.Surface((size, size), pygame.SRCALPHA)
    
    # Auto Scaling green color
    as_color = (0, 255, 0)
    
    # Draw Auto Scaling icon (simplified)
    # Draw circle
    pygame.draw.circle(surface, as_color, (size//2, size//2), size//2-2)
    
    # Draw plus sign
    pygame.draw.line(surface, (255, 255, 255), (size//2, size//4), (size//2, size*3//4), 2)
    pygame.draw.line(surface, (255, 255, 255), (size//4, size//2), (size*3//4, size//2), 2)
    
    return surface

def create_multiaz_icon(size):
    """Create a Multi-AZ icon surface"""
    surface = pygame.Surface((size, size), pygame.SRCALPHA)
    
    # Multi-AZ blue color
    ma_color = (0, 0, 255)
    
    # Draw Multi-AZ icon (simplified)
    # Draw circle
    pygame.draw.circle(surface, ma_color, (size//2, size//2), size//2-2)
    
    # Draw AZ symbol
    pygame.draw.line(surface, (255, 255, 255), (size//4, size//3), (size//2, size*2//3), 2)
    pygame.draw.line(surface, (255, 255, 255), (size//2, size*2//3), (size*3//4, size//3), 2)
    pygame.draw.line(surface, (255, 255, 255), (size//3, size//2), (size*2//3, size//2), 2)
    
    return surface
