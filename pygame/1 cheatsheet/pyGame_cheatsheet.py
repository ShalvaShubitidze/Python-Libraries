"""
to install pygame
in terminal write--> pip install pygame

Pygame Cheatsheet - A Complete Guide with Explanations
-------------------------------------------------------
This cheatsheet provides a comprehensive overview of the core functions 
and methods offered by Pygame for developing simulations, games, and interactive applications. 
It includes details for creating windows, handling events, graphics, input, sound, and more.

This script demonstrates:
✅ Initializing Pygame
✅ Creating windows
✅ Handling events (keyboard, mouse, window)
✅ Drawing objects (shapes, images, text)
✅ Animating objects
✅ Playing sound and music
✅ Handling input (keyboard, mouse)
✅ Managing time and frames
"""
import pygame

# --------------------------------------------
# 1️⃣ INITIALIZING PYGAME
# --------------------------------------------
# Initialize all Pygame modules
pygame.init()

# Initialize specific Pygame modules (e.g., for sound, joystick)
pygame.mixer.init()  # For sound
pygame.font.init()  # For fonts

# Initialize the Pygame display (used for creating windows)
pygame.display.set_mode((width, height))  # Initializes the window with specific dimensions

# --------------------------------------------
# 2️⃣ CREATING AND HANDLING WINDOWS
# --------------------------------------------
# Set the window size (width, height) and title
screen = pygame.display.set_mode((800, 600))  # Create a window with specified width and height
pygame.display.set_caption("My Game Window")  # Set the window title

# Get the window size (returns tuple: width, height)
window_size = screen.get_size()

# --------------------------------------------
# 3️⃣ HANDLING EVENTS
# --------------------------------------------
# Loop through events (key presses, mouse clicks, window events)
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()  # Quit the game
        quit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            print("Space key pressed")
    elif event.type == pygame.MOUSEBUTTONDOWN:
        print(f"Mouse clicked at {pygame.mouse.get_pos()}")

# --------------------------------------------
# 4️⃣ DRAWING OBJECTS
# --------------------------------------------
# Drawing shapes on the screen

# Fill the entire screen with a color (RGB tuple)
screen.fill((255, 255, 255))  # Fill with white color

# Draw a rectangle (color, position, width, height)
pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 150))  # Red rectangle

# Draw a circle (color, position, radius)
pygame.draw.circle(screen, (0, 255, 0), (400, 300), 50)  # Green circle

# Draw a line (color, start position, end position, width)
pygame.draw.line(screen, (0, 0, 255), (50, 50), (750, 550), 5)  # Blue line

# --------------------------------------------
# 5️⃣ DRAWING TEXT
# --------------------------------------------
# Define the font and size
font = pygame.font.Font(None, 36)  # None means default font
text = font.render('Hello, Pygame!', True, (0, 0, 0))  # Render the text

# Draw text on the screen
screen.blit(text, (300, 50))  # Blit the text at specified coordinates

# --------------------------------------------
# 6️⃣ DISPLAYING IMAGES
# --------------------------------------------
# Load an image and scale it
image = pygame.image.load('example_image.png')
image = pygame.transform.scale(image, (100, 100))  # Resize the image

# Display the image at specific coordinates
screen.blit(image, (350, 250))

# --------------------------------------------
# 7️⃣ HANDLING SOUND AND MUSIC
# --------------------------------------------
# Initialize the mixer for sound
pygame.mixer.init()

# Load and play sound (can be used for effects)
sound = pygame.mixer.Sound('sound_effect.wav')
sound.play()  # Play the sound

# Load and play background music
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.play(-1, 0.0)  # Loop music indefinitely

# Stop music or sound
pygame.mixer.music.stop()  # Stop background music
sound.stop()  # Stop the sound effect

# --------------------------------------------
# 8️⃣ HANDLING MOUSE INPUT
# --------------------------------------------
# Get mouse position (returns tuple of x, y coordinates)
mouse_pos = pygame.mouse.get_pos()

# Check if mouse button is pressed
mouse_buttons = pygame.mouse.get_pressed()
if mouse_buttons[0]:  # Left button is pressed
    print("Left mouse button pressed")

# --------------------------------------------
# 9️⃣ HANDLING KEYBOARD INPUT
# --------------------------------------------
# Check if a key is being pressed
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    print("Left arrow key is pressed")

# Get the last key pressed
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        print(f"Key pressed: {pygame.key.name(event.key)}")

# --------------------------------------------
# 🔟 HANDLING TIME AND FRAMES
# --------------------------------------------
# Creating a clock object for controlling the frame rate
clock = pygame.time.Clock()

# Control the game's frame rate (e.g., 60 frames per second)
clock.tick(60)  # Will ensure the game runs at 60 FPS

# Get the time elapsed since the last frame in milliseconds
time_passed = clock.get_time()

# --------------------------------------------
# 1️⃣1️⃣ CREATING GAME LOOP
# --------------------------------------------
# Game loop (usually run until the user closes the window)
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the loop and close the game

    # Game logic goes here
    
    # Update the display
    pygame.display.flip()

    # Frame rate control
    clock.tick(60)

pygame.quit()  # Close the Pygame window

# --------------------------------------------
# 1️⃣2️⃣ TIMERS (SYNCHRONIZING SIMULATION)
# --------------------------------------------
# Set a timer to trigger events after a delay (in milliseconds)
pygame.time.set_timer(pygame.USEREVENT, 1000)  # Trigger every 1000ms (1 second)

# Handle the timer event
for event in pygame.event.get():
    if event.type == pygame.USEREVENT:
        print("Timer triggered")

# --------------------------------------------
# 1️⃣3️⃣ COLLISION DETECTION
# --------------------------------------------
# Check if two objects collide (returns True if they do)
rect1 = pygame.Rect(100, 100, 50, 50)  # Create a rectangle at position (100, 100)
rect2 = pygame.Rect(120, 120, 50, 50)  # Create another rectangle at position (120, 120)

# Check if the rectangles collide
if rect1.colliderect(rect2):
    print("Collision detected!")

# --------------------------------------------
# ✅ SUMMARY
# --------------------------------------------
"""
✅ How to initialize Pygame and set up a window.
✅ How to handle different types of events (keyboard, mouse, quit).
✅ How to draw shapes (rectangles, circles, lines) and display text.
✅ How to work with images and scale them for display.
✅ How to handle sound effects and background music.
✅ How to check for mouse clicks and get mouse position.
✅ How to get and handle keyboard input.
✅ How to control the frame rate using a clock object.
✅ How to synchronize simulations with timers and handle collisions.
"""

pygame.quit()
print("\n🎉 Pygame Cheatsheet Execution Complete! 🚀")
