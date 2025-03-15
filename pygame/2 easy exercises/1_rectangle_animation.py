'''
======================================
1️⃣ Simple Rectangle Animation
======================================
📌 Scenario:
Create a window with a blue rectangle that moves across the screen. 
Make it bounce back when it reaches the window edge.

🔹 **Concepts Used:**
   - Window setup
   - Event handling
   - Rectangle drawing
   - Frame rate control
   - Movement

🧠 **Think About It!**
Before looking at the solution, try to answer:
1. How do you move the rectangle across the screen?
2. How do you detect when the rectangle reaches the window edge?
3. How do you make the rectangle bounce back?

🛠 **Try to complete this yourself, then check the solution below!** 🛠

======================================
✅ Solution
======================================
'''

import pygame

# Initialize pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Bouncing Rectangle")

# Create a rectangle (x, y, width, height)
rect = pygame.Rect(100, 300, 100, 50)

# Set movement speed
rect_speed = 5  

# Create a clock to control frame rate
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    # Handle events (check if the window is closed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Move the rectangle
    rect.x += rect_speed  

    # Bounce back when hitting the window edges
    if rect.x > screen.get_width() - rect.width or rect.x < 0:
        rect_speed = -rect_speed

    # Draw the rectangle
    pygame.draw.rect(screen, (0, 0, 255), rect)  # Blue rectangle

    # Update the screen
    pygame.display.update()

    # Control frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
