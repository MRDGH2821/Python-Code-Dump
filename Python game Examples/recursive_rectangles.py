"""
 Recursively draw rectangles.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""

import pygame

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)


def recursive_draw(x, y, width, height):
    """Recursive rectangle function."""
    pygame.draw.rect(screen, black, [x, y, width, height], 1)
    # Is the rectangle wide enough to draw again?
    if width > 14:
        # Scale down
        x += width * 0.1
        y += height * 0.1
        width *= 0.8
        height *= 0.8
        # Recursively draw again
        recursive_draw(x, y, width, height)


pygame.init()
# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
    # Set the screen background
    screen.fill(white)
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    recursive_draw(0, 0, 700, 500)
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # Limit to 60 frames per second
    clock.tick(60)
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
