# Amazon Q CLI Prompt for AWS-Themed Snake Game

## Initial Game Creation Prompt

```
I want to create an AWS-themed Snake game using Python and Pygame. Here are the specific requirements:

**Game Concept:**
- Classic Snake gameplay but with AWS cloud theming
- Snake represents data flowing through AWS services
- Food items are AWS service icons (EC2, S3, Lambda, etc.)
- Power-ups based on AWS services
- Obstacles representing network latency or service outages

**Technical Requirements:**
- Use Python with Pygame library
- Window size: 800x600 pixels
- Grid-based movement (20x20 pixel cells)
- 60 FPS smooth gameplay
- Score tracking and high score persistence

**AWS Theming Details:**
- Snake: Blue gradient segments representing data packets
- Background: AWS console dark theme (#232F3E)
- Food items: Colorful AWS service icons (use simple geometric shapes as placeholders)
- UI elements: AWS orange (#FF9900) for score and menus

**Game Features to Include:**
1. Basic snake movement (arrow keys)
2. Food collection that grows the snake
3. Wall and self-collision detection
4. Score system (10 points per food)
5. Game over screen with restart option
6. Start menu with game title

**AWS-Specific Elements:**
- Snake segments could have AWS service labels
- Different food types worth different points
- Sound effects for "service deployment" (eating food)
- Power-ups that temporarily boost speed or provide shields

Please create a complete, working game with proper code structure, comments, and error handling. Start with the basic game loop and core mechanics first.
```

## Follow-up Prompts for Enhancement

### For Adding AWS Service Icons

```
Now let's enhance the game with specific AWS service representations:

- Replace generic food with AWS service icons using simple colored rectangles/circles
- EC2: Orange rectangle (represents compute)
- S3: Green circle (represents storage)  
- Lambda: Yellow triangle (represents serverless)
- RDS: Blue diamond (represents database)
- Each service type gives different points: EC2(10), S3(15), Lambda(20), RDS(25)

Add a legend in the corner showing what each shape represents and its point value.
```

### For Power-ups System

```
Add AWS-themed power-ups that appear randomly:

1. **CloudFront Boost**: Purple star - increases snake speed for 5 seconds
2. **Shield (WAF)**: Red hexagon - makes snake invulnerable to walls for 3 seconds  
3. **Auto Scaling**: Green plus sign - temporarily slows down snake for easier control
4. **Multi-AZ**: Blue cross - gives extra life (can hit wall once without dying)

Each power-up should have visual feedback when activated and a timer showing remaining duration.
```

### For Advanced Features

```
Let's add more AWS-themed gameplay mechanics:

1. **Availability Zones**: Divide the screen into colored zones, each giving score multipliers
2. **Service Outages**: Random red "X" obstacles that appear and disappear
3. **Load Balancer**: Special food that splits the snake temporarily into multiple segments
4. **Cost Optimization**: Timer that reduces score if snake moves too slowly (encourages efficiency)
5. **Region Selection**: Menu to choose different "regions" (difficulty levels)

Add appropriate visual indicators and sound effects for each mechanic.
```

### For Polish and Completion

```
Final enhancement requests:

1. Add a proper game menu with:
   - AWS-styled logo/title
   - High score display
   - Instructions screen explaining AWS themes
   - Settings for difficulty/sound

2. Improve graphics:
   - Add simple animations for power-up collection
   - Snake head should look different from body segments
   - Particle effects when eating AWS services
   - Screen shake on collisions

3. Add sound effects:
   - Background music (optional)
   - Collection sounds for different AWS services
   - Power-up activation sounds
   - Game over sound

4. Code optimization:
   - Clean up code structure
   - Add comprehensive comments explaining AWS theming choices
   - Include error handling and edge cases
   - Make code easily modifiable for different AWS services

Please provide the complete, polished game ready for the Amazon Q CLI challenge submission.
```

## Tips for Using These Prompts

1. **Start with the initial prompt** - Get the basic game working first
2. **Test each addition** - Make sure each enhancement works before moving to the next
3. **Be specific** - Amazon Q CLI works better with detailed requirements
4. **Ask for explanations** - Request comments explaining the AWS theming choices
5. **Iterate gradually** - Add features one at a time rather than all at once

## Documentation Prompt

```
Create comprehensive documentation for this AWS-themed Snake game including:

1. **README.md** with:
   - Game description and AWS theming explanation
   - Installation instructions
   - How to play guide
   - AWS services featured in the game
   - Screenshots/ASCII art of gameplay

2. **Developer notes** explaining:
   - Why specific AWS services were chosen
   - How the theming enhances the classic Snake gameplay
   - Technical decisions made during development
   - Future enhancement ideas

This documentation will be perfect for your blog post and social media sharing for the Amazon Q CLI challenge.
```

Remember to ask Amazon Q CLI to explain its choices and provide multiple options when you're not satisfied with the initial results. Good luck with the challenge!
