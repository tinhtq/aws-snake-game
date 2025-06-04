import pygame
import random
from assets.images.icons.icon_loader import get_service_icon, get_powerup_icon

# AWS Service Types
class AWSServiceType:
    EC2 = 0
    S3 = 1
    LAMBDA = 2
    RDS = 3
    
    @staticmethod
    def get_random():
        return random.randint(0, 3)
    
    @staticmethod
    def get_color(service_type):
        colors = {
            AWSServiceType.EC2: (240, 173, 0),      # Orange for EC2
            AWSServiceType.S3: (40, 167, 69),       # Green for S3
            AWSServiceType.LAMBDA: (255, 215, 0),   # Yellow for Lambda
            AWSServiceType.RDS: (0, 123, 255)       # Blue for RDS
        }
        return colors.get(service_type, (255, 255, 255))
    
    @staticmethod
    def get_points(service_type):
        points = {
            AWSServiceType.EC2: 10,     # EC2: 10 points
            AWSServiceType.S3: 15,      # S3: 15 points
            AWSServiceType.LAMBDA: 20,  # Lambda: 20 points
            AWSServiceType.RDS: 25      # RDS: 25 points
        }
        return points.get(service_type, 10)
    
    @staticmethod
    def get_shape(service_type):
        shapes = {
            AWSServiceType.EC2: "rectangle",    # EC2: Rectangle
            AWSServiceType.S3: "circle",        # S3: Circle
            AWSServiceType.LAMBDA: "triangle",  # Lambda: Triangle
            AWSServiceType.RDS: "diamond"       # RDS: Diamond
        }
        return shapes.get(service_type, "rectangle")
    
    @staticmethod
    def get_name(service_type):
        names = {
            AWSServiceType.EC2: "EC2",
            AWSServiceType.S3: "S3",
            AWSServiceType.LAMBDA: "Lambda",
            AWSServiceType.RDS: "RDS"
        }
        return names.get(service_type, "Unknown")
    
    @staticmethod
    def get_description(service_type):
        descriptions = {
            AWSServiceType.EC2: "Amazon Elastic Compute Cloud (EC2) provides resizable compute capacity in the cloud. It's like having virtual servers that you can scale up or down based on your needs.",
            AWSServiceType.S3: "Amazon Simple Storage Service (S3) is object storage built to store and retrieve any amount of data. It's like a highly durable and scalable file system in the cloud.",
            AWSServiceType.LAMBDA: "AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume - no charge when your code is not running.",
            AWSServiceType.RDS: "Amazon Relational Database Service (RDS) makes it easy to set up, operate, and scale a relational database in the cloud. It provides cost-efficient and resizable capacity."
        }
        return descriptions.get(service_type, "An AWS service that helps you build scalable applications.")
    
    @staticmethod
    def get_icon(service_type, grid_size):
        return get_service_icon(service_type, grid_size)

class AWSService:
    def __init__(self, grid_size):
        self.position = (0, 0)
        self.service_type = AWSServiceType.get_random()
        self.color = AWSServiceType.get_color(self.service_type)
        self.points = AWSServiceType.get_points(self.service_type)
        self.shape = AWSServiceType.get_shape(self.service_type)
        self.grid_size = grid_size
        self.icon = AWSServiceType.get_icon(self.service_type, grid_size)
        self.randomize_position(grid_width=40, grid_height=30)  # 800/20 = 40, 600/20 = 30
        
    def randomize_position(self, grid_width, grid_height):
        self.position = (random.randint(0, grid_width - 1), random.randint(0, grid_height - 1))
        
    def render(self, surface):
        x = self.position[0] * self.grid_size
        y = self.position[1] * self.grid_size
        
        # Draw the icon
        surface.blit(self.icon, (x, y))

# AWS Power-ups
class PowerUpType:
    CLOUDFRONT = 0  # Speed boost
    WAF = 1         # Wall invulnerability
    AUTO_SCALING = 2  # Slow down (easier control)
    MULTI_AZ = 3    # Extra life
    
    @staticmethod
    def get_random():
        return random.randint(0, 3)
    
    @staticmethod
    def get_color(powerup_type):
        colors = {
            PowerUpType.CLOUDFRONT: (148, 0, 211),    # Purple for CloudFront
            PowerUpType.WAF: (255, 0, 0),             # Red for WAF
            PowerUpType.AUTO_SCALING: (0, 255, 0),    # Green for Auto Scaling
            PowerUpType.MULTI_AZ: (0, 0, 255)         # Blue for Multi-AZ
        }
        return colors.get(powerup_type, (255, 255, 255))
    
    @staticmethod
    def get_shape(powerup_type):
        shapes = {
            PowerUpType.CLOUDFRONT: "star",     # CloudFront: Star
            PowerUpType.WAF: "hexagon",         # WAF: Hexagon
            PowerUpType.AUTO_SCALING: "plus",   # Auto Scaling: Plus sign
            PowerUpType.MULTI_AZ: "cross"       # Multi-AZ: Cross
        }
        return shapes.get(powerup_type, "circle")
    
    @staticmethod
    def get_name(powerup_type):
        names = {
            PowerUpType.CLOUDFRONT: "CloudFront Boost",
            PowerUpType.WAF: "Shield (WAF)",
            PowerUpType.AUTO_SCALING: "Auto Scaling",
            PowerUpType.MULTI_AZ: "Multi-AZ"
        }
        return names.get(powerup_type, "Unknown")
    
    @staticmethod
    def get_duration(powerup_type):
        durations = {
            PowerUpType.CLOUDFRONT: 5,    # 5 seconds for CloudFront
            PowerUpType.WAF: 3,           # 3 seconds for WAF
            PowerUpType.AUTO_SCALING: 7,  # 7 seconds for Auto Scaling
            PowerUpType.MULTI_AZ: 0       # Multi-AZ is instant (extra life)
        }
        return durations.get(powerup_type, 5)
    
    @staticmethod
    def get_icon(powerup_type, grid_size):
        return get_powerup_icon(powerup_type, grid_size)

class PowerUp:
    def __init__(self, grid_size):
        self.position = (0, 0)
        self.active = False
        self.powerup_type = PowerUpType.get_random()
        self.color = PowerUpType.get_color(self.powerup_type)
        self.shape = PowerUpType.get_shape(self.powerup_type)
        self.grid_size = grid_size
        self.icon = PowerUpType.get_icon(self.powerup_type, grid_size)
        self.spawn_time = 0
        self.duration = PowerUpType.get_duration(self.powerup_type)
        
    def activate(self):
        self.active = False
        return self.powerup_type, self.duration
        
    def randomize_position(self, grid_width, grid_height):
        self.position = (random.randint(0, grid_width - 1), random.randint(0, grid_height - 1))
        self.active = True
        
    def render(self, surface):
        if not self.active:
            return
            
        x = self.position[0] * self.grid_size
        y = self.position[1] * self.grid_size
        
        # Draw the icon
        surface.blit(self.icon, (x, y))
