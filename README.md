# AWS Snake Game

An AWS-themed version of the classic Snake game, where you control a data packet snake collecting AWS services across the cloud!

> **Note**: This game was created using Amazon Q CLI. The prompting sentences used to generate this game can be found in the `prompting/requirement.md` file.

## Game Description

AWS Snake Game reimagines the classic Snake gameplay with AWS cloud theming:

- **Snake**: Represents data flowing through AWS services, visualized as blue gradient segments
- **Food Items**: AWS service icons (EC2, S3, Lambda, RDS) with different point values
- **Power-ups**: Special AWS-themed abilities that provide temporary advantages
- **Theme**: AWS console dark theme with AWS orange accents

## Installation

1. Ensure you have Python 3.6+ installed
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
   or
   ```
   pip install pygame
   ```
3. Clone or download this repository
4. Run the game:
   ```
   python main.py
   ```

## How to Play

- Use **arrow keys** to control the snake's direction
- Collect AWS service icons to grow your snake and earn points
- Different AWS services are worth different points:
  - **EC2** (Orange Rectangle): 10 points
  - **S3** (Green Circle): 15 points
  - **Lambda** (Yellow Triangle): 20 points
  - **RDS** (Blue Diamond): 25 points
- Collect power-ups for special abilities:
  - **CloudFront Boost** (Purple Star): Increases snake speed for 5 seconds
  - **Shield (WAF)** (Red Hexagon): Makes snake invulnerable to walls for 3 seconds
  - **Auto Scaling** (Green Plus): Temporarily slows down snake for easier control (7 seconds)
  - **Multi-AZ** (Blue Cross): Gives extra life (can hit wall once without dying)
- Avoid colliding with the walls or your own tail

## AWS Services Featured

The game features several AWS services represented as collectible items:

- **Amazon EC2**: Elastic Compute Cloud - represented by orange rectangles
- **Amazon S3**: Simple Storage Service - represented by green circles
- **AWS Lambda**: Serverless compute service - represented by yellow triangles
- **Amazon RDS**: Relational Database Service - represented by blue diamonds

Power-ups are also themed after AWS services:

- **Amazon CloudFront**: Content delivery network - provides speed boost
- **AWS WAF**: Web Application Firewall - provides temporary invulnerability
- **AWS Auto Scaling**: Adjusts capacity to maintain performance - slows down snake for better control
- **Multi-AZ Deployment**: High availability feature - provides an extra life

## How to Add Custom AWS Icons

To use actual AWS service icons in the game:

1. Place your icon image files in the `assets/images/icons` directory
2. Name the files according to the service:
   - `ec2.png` - For EC2 service
   - `s3.png` - For S3 service
   - `lambda.png` - For Lambda service
   - `rds.png` - For RDS service
   - `cloudfront.png` - For CloudFront power-up
   - `waf.png` - For WAF power-up
   - `autoscaling.png` - For Auto Scaling power-up
   - `multiaz.png` - For Multi-AZ power-up
3. The game will automatically use these images if they exist
4. If an image file is missing, the game will fall back to the programmatically generated icons

## Developer Notes

This game was created as part of the Amazon Q CLI challenge. The AWS theming was chosen to demonstrate how cloud services can be represented in a fun, interactive way.

### Technical Implementation

- Built with Python and Pygame
- Grid-based movement system (20x20 pixel cells)
- AWS-themed color scheme (#232F3E background, #FF9900 accents)
- Object-oriented design with separate classes for Snake, AWS Services, and Power-ups

### Future Enhancements

- Add more AWS services as collectible items
- Implement different "regions" as game levels
- Add sound effects for service collection and power-up activation
- Create a more detailed scoring system based on AWS service pricing

## Credits

Created by [Your Name] using Python and Pygame for the Amazon Q CLI challenge.
