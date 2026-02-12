import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Hello Pygame")

screen.fill((255, 255, 255))

pygame.draw.rect(screen, (0,   0, 255),
                 [0, 100, 200, 30])
pygame.draw.polygon(screen, (0, 0, 255), 
                    [[0, 200], [199, 130],
                     [0, 130]])


pygame.draw.rect(screen, (0,   0, 255),
                 [300, 250, 200, 30])

pygame.draw.polygon(screen, (0, 0, 255), 
                    [[300, 280], [500, 280],
                     [500, 330]])

pygame.display.update()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()