import pygame
import spritesheet
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 1200, 675
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame")

screenSurface =pygame.Surface((WIDTH,HEIGHT), pygame.SRCALPHA)
clock = pygame.time.Clock()

# Colors
PLAYER_COLOR = (0, 200, 255)
BULLET_COLOR = (255, 50, 50)
PLATFORM_COLOR = (0, 0, 255)
BG_COLOR = (30, 30, 30)
BLACK = (0,0,0)
MENY_BG_COLOR = (10,10,200)

BUTTON_COLOR = (70, 130, 180)
HOVER_COLOR = (100, 170, 220)
TEXT_COLOR = (255, 255, 255)

# Font
font = pygame.font.SysFont(None, 36)

world_x = 0  
world_y = 0
dheight = 0
dwidth = 0 
height_level = 1

# Player setup
square_width = 60
square_height = 110
player = pygame.Rect(WIDTH // 2 - square_width // 2+dwidth, HEIGHT- 80- square_height +dheight, square_width, square_height)

y_velocity = 0
gravity = 0.5
jump_strength = -12
on_ground = False
double_jump = True
t = 1



speed = 1


teleport_timer = pygame.USEREVENT + 1


_Idle = pygame.image.load('PNGSheets/_Idle.png').convert_alpha()
_run = pygame.image.load('PNGSheets/_Run.png').convert_alpha()
_run_left = pygame.image.load('PNGSheets/_Run_left.png').convert_alpha()
sprite_sheet = spritesheet.SpritreSheet(_Idle)


animation_list = []
animation_steps = 10
last_update = pygame.time.get_ticks()
animation_cooldown = 100
frame = 0





# objects
solids = [
    pygame.Rect(-WIDTH * 10 +dwidth, HEIGHT - 80, WIDTH * 20, 100),  # ground
    pygame.Rect(-300+dwidth, 550+dheight, 150, 30),
    pygame.Rect(1100+dwidth, 500+dheight, 150, 30),
    pygame.Rect(600+dwidth, 300+dheight, 150, 30),
    pygame.Rect(400+dwidth, 170+dheight, 150, 60),
    pygame.Rect(-1100+dwidth, 110+dheight, 1500, 120),
    pygame.Rect(1100+dwidth, 120+dheight, 1500, 80),
    pygame.Rect(800+dwidth, 350+dheight, 200, 30)
    ]
# Bullets 
bullets = []
bullet_speed = 12
bullet_radius = 5
bullet_cooldown = 0



# Button class
class Button:
    def __init__(self, text, x, y, w, h):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self, surface):
        color = HOVER_COLOR if self.rect.collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR
        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2)
        text_surf = font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )

# Create buttons
buttons = [
    Button("Play", WIDTH/2-WIDTH/10, HEIGHT/2-WIDTH/40-HEIGHT/8, WIDTH/5, WIDTH/20),
    Button("Options", WIDTH/2-WIDTH/10, HEIGHT/2-WIDTH/40, WIDTH/5, WIDTH/20),
    Button("Quit", WIDTH/2-WIDTH/10, HEIGHT/2-WIDTH/40+HEIGHT/8, WIDTH/5, WIDTH/20),
]
option = [
    Button("Menu", WIDTH/2-WIDTH/10, HEIGHT/2-WIDTH/40-HEIGHT/8, WIDTH/5, WIDTH/20),
    Button("Size +", WIDTH/2-WIDTH/10-WIDTH/9, HEIGHT/2-WIDTH/40, WIDTH/5, WIDTH/20),    
    Button("Size -", WIDTH/2-WIDTH/10 +WIDTH/9, HEIGHT/2-WIDTH/40, WIDTH/5, WIDTH/20),
    Button("1200x675", WIDTH/2-WIDTH/10, HEIGHT/2-WIDTH/40+HEIGHT/8, WIDTH/5, WIDTH/20),
    Button("1920x1080", WIDTH/2-WIDTH/10, HEIGHT/2-WIDTH/40+HEIGHT/4, WIDTH/5, WIDTH/20)
]

meny = True
options = False

# Game Loop
while True:
    animation_list = []
    for x in range(animation_steps):
        animation_list.append(sprite_sheet.get_image(x, 120, 80, 3, BLACK))
    sprite_sheet = spritesheet.SpritreSheet(_Idle)
        
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()




        for button in buttons:
            if button.clicked(event) and meny == True and options == False:
                print(f"{button.text} clicked!")

                if button.text == "Quit":
                    pygame.quit()
                    sys.exit()

                if button.text == "Play":
                    meny = False
                    solids = [
                        pygame.Rect(-WIDTH * 10 +dwidth, HEIGHT - 80, WIDTH * 20, 100),  # ground
                        pygame.Rect(-300+dwidth, 550+dheight, 150, 30),
                        pygame.Rect(1100+dwidth, 500+dheight, 150, 30),
                        pygame.Rect(600+dwidth, 300+dheight, 150, 30),
                        pygame.Rect(400+dwidth, 170+dheight, 150, 60),
                        pygame.Rect(-1100+dwidth, 110+dheight, 1500, 120),
                        pygame.Rect(1100+dwidth, 120+dheight, 1500, 80),
                        pygame.Rect(800+dwidth, 350+dheight, 200, 30)
                        ]
                    player = pygame.Rect(player.x +dwidth/2, player.y +dheight, square_width, square_height)
                    pygame.display.flip()

                if button.text == "Options":
                    options = True

        for button in option:
            if button.clicked(event) and options == True and meny == True:
                print(f"{button.text} clicked!")

                if button.text == "Menu":
                    options = False

                if button.text == "Size +" and HEIGHT < 1080:
                    WIDTH += 16
                    HEIGHT += 9
                    dheight += 9
                    dwidth += 8                        
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    screenSurface =pygame.Surface((WIDTH,HEIGHT), pygame.SRCALPHA)


                if button.text == "Size -" and 600 < HEIGHT:
                    WIDTH -= 16
                    HEIGHT -= 9
                    dheight -= 9
                    dwidth -= 8
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    screenSurface =pygame.Surface((WIDTH,HEIGHT), pygame.SRCALPHA)
                    pygame.display.flip()
                if button.text == "1200x675":
                    WIDTH = 1200
                    HEIGHT = 675
                    dheight = 0
                    dwidth = 0                        
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    screenSurface =pygame.Surface((WIDTH,HEIGHT), pygame.SRCALPHA)
                    pygame.display.flip()
        # Jump
        if event.type  == pygame.KEYDOWN and on_ground:
            if event.key == pygame.K_SPACE or keys[pygame.K_UP]:
                y_velocity = jump_strength
                on_ground = False
                double_jump = True
        

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                meny = not meny

    player_center = [player.centerx, player.centery]

    # Movement Input

    dx = 0
    

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        dx = current_speed
        sprite_sheet = spritesheet.SpritreSheet(_run_left)




    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        dx = -current_speed
        sprite_sheet = spritesheet.SpritreSheet(_run)
    if keys[pygame.K_LSHIFT] and on_ground and dx != 0:

        current_speed = 10
        jump_strength = -15
    else: 
        jump_strength = -13
        current_speed = 8



    # Move world horizontally
    if meny == False:
        world_x += dx


    # Horizontal Collision and moving of world
    if dx != 0 and meny == False:
        for solid in solids:
            solid_screen = solid.move(world_x, 0)

            if player.colliderect(solid_screen):
                if dx > 0:
                    world_x -= current_speed
                elif dx < 0:
                    world_x += current_speed


    # Apply Gravity
    if meny == False:
        y_velocity += gravity
        player.y += y_velocity

        on_ground = False


    # Vertical Collision
    for solid in solids:
        solid_screen = solid.move(world_x, 0)

        if player.colliderect(solid_screen):

            if y_velocity > 0:  # Falling
                player.bottom = solid_screen.top
                y_velocity = 0
                on_ground = True

            elif y_velocity < 0:  # Jumping up
                player.top = solid_screen.bottom
                y_velocity = 0


    # teleports the player upp or down
    if (player.y <= -50 and height_level == 1) or keys[pygame.K_LEFT] :
        pygame.time.set_timer(teleport_timer, 5000)
        height_level = 2
        dheight += 550
        player.y += 550

        solids = [

            pygame.Rect(-1100+dwidth, 90+dheight, 1500, 140),
            pygame.Rect(1100+dwidth, 120+dheight, 1500, 80),

            pygame.Rect(800+dwidth, -30+dheight, 200, 30)

            ]
        dheight = 0
        player = pygame.Rect(player.x +dwidth/2, player.y +dheight, square_width, square_height)
        pygame.display.flip()

    if (player.y >= 600 and height_level == 2 and height_level == 2) or keys[pygame.K_LEFT] :
        height_level = 1
        player.y -= 520

        solids = [
            pygame.Rect(-WIDTH * 10 +dwidth, HEIGHT - 80, WIDTH * 20, 100),  # ground
            pygame.Rect(-300+dwidth, 550+dheight, 150, 30),
            pygame.Rect(1100+dwidth, 500+dheight, 150, 30),
            pygame.Rect(600+dwidth, 300+dheight, 150, 30),
            pygame.Rect(400+dwidth, 170+dheight, 150, 60),
            pygame.Rect(-1100+dwidth, 110+dheight, 1500, 120),
            pygame.Rect(1100+dwidth, 120+dheight, 1500, 80),
            pygame.Rect(800+dwidth, 350+dheight, 200, 30)
            ]
        dheight = 0
        player = pygame.Rect(player.x +dwidth/2, player.y +dheight, square_width, square_height)
        pygame.display.flip()
    




    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame +=1
        last_update = current_time
        if frame >= len(animation_list):
            frame = 0
    # Drawing
    screen.fill(BG_COLOR)


    # Draw solids
    for solid in solids:
        draw_rect = solid.move(world_x, 0)
        pygame.draw.rect(screen, PLATFORM_COLOR, draw_rect)

    # player hitbox
    #pygame.draw.rect(screen, PLAYER_COLOR, player)

    #player drawing

    screen.blit(animation_list[frame],(player.x- 195 +square_width ,player.y-240+square_height))


    if meny:
        screenSurface.fill((30,30,30,128))                         # notice the alpha value in the color
        screen.blit(screenSurface, (0,0))

        #draw buttons
    if meny and options == False:    
        for button in buttons:
            button.draw(screen)

    if options == True:    
        for button in option:
            button.draw(screen)
            
    pygame.display.flip()
    dt = clock.tick(60)