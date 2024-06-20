# imports
import pygame
import requests

# initializing imported module
pygame.init()

# displaying a window of height
# 800 and width 650
surface = pygame.display.set_mode((800, 650))

pygame.display.set_caption('Test Window')

# Initializing RGB Color
color = (80, 80, 200)

# Drawing Rectangle
pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))

# Changing surface color
surface.fill(color)
pygame.display.flip()

# creating a bool value which checks
# if game is running
running = True

# keep game running till running is true
while running:

    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():

        # if event is of type quit then
        # set running bool to false
        if event.type == pygame.QUIT:
            running = False
