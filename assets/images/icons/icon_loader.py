import os
import pygame
from assets.images.services.ec2 import create_ec2_icon
from assets.images.services.s3 import create_s3_icon
from assets.images.services.lambda_service import create_lambda_icon
from assets.images.services.rds import create_rds_icon
from assets.images.services.powerups import (
    create_cloudfront_icon, create_waf_icon, 
    create_autoscaling_icon, create_multiaz_icon
)

# Base path for icon images
ICONS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "icons")

def load_image(filename, size):
    """Load an image and scale it to the specified size"""
    try:
        # Try to load the image file
        path = os.path.join(ICONS_PATH, filename)
        if os.path.exists(path):
            image = pygame.image.load(path).convert_alpha()
            return pygame.transform.scale(image, (size, size))
        else:
            return None
    except (pygame.error, FileNotFoundError):
        return None

def get_service_icon(service_type, size):
    """Get an AWS service icon, either from file or generated"""
    # Map service types to filenames
    filenames = {
        0: "ec2.png",  # EC2
        1: "s3.png",   # S3
        2: "lambda.png",  # Lambda
        3: "rds.png"   # RDS
    }
    
    # Try to load the image file
    if service_type in filenames:
        image = load_image(filenames[service_type], size)
        if image:
            return image
    
    # Fall back to generated icons if image loading fails
    generators = {
        0: create_ec2_icon,
        1: create_s3_icon,
        2: create_lambda_icon,
        3: create_rds_icon
    }
    
    if service_type in generators:
        return generators[service_type](size)
    
    # Default to EC2 icon if service type is unknown
    return create_ec2_icon(size)

def get_powerup_icon(powerup_type, size):
    """Get a power-up icon, either from file or generated"""
    # Map powerup types to filenames
    filenames = {
        0: "cloudfront.png",  # CloudFront
        1: "waf.png",         # WAF
        2: "autoscaling.png", # Auto Scaling
        3: "multiaz.png"      # Multi-AZ
    }
    
    # Try to load the image file
    if powerup_type in filenames:
        image = load_image(filenames[powerup_type], size)
        if image:
            return image
    
    # Fall back to generated icons if image loading fails
    generators = {
        0: create_cloudfront_icon,
        1: create_waf_icon,
        2: create_autoscaling_icon,
        3: create_multiaz_icon
    }
    
    if powerup_type in generators:
        return generators[powerup_type](size)
    
    # Default to CloudFront icon if powerup type is unknown
    return create_cloudfront_icon(size)
