import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

platform = 200
# Set up the game window
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame")

clock = pygame.time.Clock()

#background variabler
x = 0
y = 0

#Høyder for ulike steder
ground_y = HEIGHT - 80
left_rect = -75

# Square settings
square_size = 50
square_x = WIDTH // 2 -square_size
square_y = square_size + ground_y
speed = 8

#hopp variabler
y_velocity = 0
gravity = 0.6
jump_strength = -12
on_ground = False



screen.fill((255, 255, 255))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x += speed
    if keys[pygame.K_d]:
        x -= speed
    if keys[pygame.KMOD_LSHIFT]:
        speed = 10
    if keys[pygame.K_SPACE] and on_ground:
        y_velocity = jump_strength
        on_ground = False
        

    # Apply gravity
    y_velocity += gravity
    square_y += y_velocity

    # Collision with ground
    if square_y + square_size >= ground_y:
        square_y = ground_y - square_size
        y_velocity = 0
        on_ground = True

    if square_y + square_size >= ground_y-75 and x>52 and x<290:
        square_y = ground_y - square_size+left_rect
        y_velocity = 0
        on_ground = True

    # Keep square on screen
    square_x = max(0, min(WIDTH - square_size, square_x))
    square_y = max(0, min(HEIGHT - square_size, square_y))

    # Drawing
    screen.fill((30, 30, 30))  # background


    pygame.draw.rect(screen, (0,   0, 255),
                    [(x)+0, (y)+650, 200, 100])




    pygame.draw.rect(screen, (0,   0, 255),
                    [(x)-WIDTH*10, (y)+(HEIGHT)-80, WIDTH*20, 200])



    pygame.draw.polygon(screen, (50, 100, 100), 
                        [[(x)+300, (y)+280], [(x)+500, (y)+280],
                        [(x)+500, (y)+330]])

    #spiller
    pygame.draw.rect(
        screen,
        (0, 100, 255),
        (square_x, square_y, square_size, square_size)
    )

    pygame.display.flip()
    clock.tick(30)