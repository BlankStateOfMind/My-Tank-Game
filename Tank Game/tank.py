from cmath import pi
from tkinter import CENTER
from turtle import position, width
import pygame
import random

pygame.init()

WIDTH = 700
HEIGHT = 700
x = WIDTH
y = HEIGHT
screen = pygame.display.set_mode((WIDTH, HEIGHT))

x = 200
y = 200

FPS = pygame.time.Clock()

#tank size
tank_size = 50

#tank size winner
tank_size_winner = 120

#heart size
heart_size = 30

#reinforement heart size
r_heart_size = 40

#tanks lives
lives_0 = 3
lives_1 = 3

#fonts
font = pygame.font.Font('fonts/myfont.ttf', 30)
font2 = pygame.font.Font('fonts/myfont.ttf', 20)

#sounds
hit_sound = pygame.mixer.Sound('sounds/hit.mp3')
select_sound = pygame.mixer.Sound('sounds/select.mp3')
shot_sound = pygame.mixer.Sound('sounds/shot.mp3')
menu_sound = pygame.mixer.Sound('sounds/menu.mp3')
pygame.mixer.music.set_volume(2.3)


#heart photos
heart_img_0 = pygame.image.load('photos/heart_0.png')
heart_scale_0 = pygame.transform.scale(heart_img_0, (heart_size, heart_size))
heart_img_1 = pygame.image.load('photos/heart_1.png')
heart_scale_1 = pygame.transform.scale(heart_img_1, (heart_size, heart_size))

#reinforcement heart
r_heart_img = pygame.image.load('photos/reinforcement_heart.png')
r_heart_img_scale = pygame.transform.scale(r_heart_img, (r_heart_size, r_heart_size))

heart_img_bonus = pygame.image.load('photos/reinforcement_heart.png')
heart_img_bonus = pygame.transform.scale(heart_img_bonus, (r_heart_size, r_heart_size))
heart_c = heart_img_bonus.get_rect(center=(WIDTH//2, HEIGHT//2))

#bg colors
blue_bg = pygame.image.load("photos/skyblue_bg.png")
pink_bg = pygame.image.load("photos/pink_bg.png")
black_bg = pygame.image.load("photos/black_bg.jpg")
green_bg = pygame.image.load("photos/green_bg.jpg")

#bg transform scale
blue_bg_scale = pygame.transform.scale(blue_bg, (WIDTH, HEIGHT))
pink_bg_scale = pygame.transform.scale(pink_bg, (WIDTH, HEIGHT))
black_bg_scale = pygame.transform.scale(black_bg, (WIDTH, HEIGHT))
green_bg_scale = pygame.transform.scale(green_bg, (WIDTH, HEIGHT))

#bg photo
rand_img = random.choice([blue_bg_scale, pink_bg_scale, black_bg_scale, green_bg_scale])

# bg_photo = pygame.image.load('photos/green_bg.png')
# bg_photo_scale = pygame.transform.scale(bg_photo, (WIDTH, HEIGHT))


#tank 1
tank_img_0 = pygame.image.load('photos/tank_0.png')
tank_img_0 = pygame.transform.scale(tank_img_0, (tank_size, tank_size))
tank_img_rotate_0 = tank_img_0
tank_0 = tank_img_0.get_rect(center=(WIDTH-tank_size, HEIGHT-tank_size))

# #tank size for winner image
# tank_0 = tank_img_0.get_rect(center=(tank_size_winner / 2, tank_size_winner / 2))

#tank 2
tank_img_1 = pygame.image.load('photos/tank_1.png')
tank_img_1 = pygame.transform.scale(tank_img_1, (tank_size, tank_size))
tank_img_rotate_1 = pygame.transform.rotate(tank_img_1, 180)
tank_1 = tank_img_1.get_rect(center=(tank_size // 1, tank_size // 1))


# #displaying blocks and walls on screen
# block1 = pygame.Surface((90, 100)) #Its width and height
# block1.fill('brown')

# block2 = pygame.Surface((90, 100)) #Its width and height
# block2.fill('burlywood4')

# block3 = pygame.Surface((90, 100)) #Its width and height
# block3.fill('brown')

# block4 = pygame.Surface((90, 100)) #Its width and height
# block4.fill('burlywood4')

# block5 = pygame.Surface((90, 100)) #Its width and height
# block5.fill('burlywood4')

# block6 = pygame.Surface((90, 100)) #Its width and height
# block6.fill('brown')

# block7 = pygame.Surface((90, 100)) #Its width and height
# block7.fill('white')

# block8 = pygame.Surface((90, 100)) #Its width and height
# block8.fill('burlywood4')

# block9 = pygame.Surface((90, 100)) #Its width and height
# block9.fill('brown')

walls = [pygame.Rect(150, 100, 125, 185), pygame.Rect(150, 400, 125, 185), pygame.Rect(425, 100, 125, 185),
        pygame.Rect(425, 400, 125, 185), pygame.Rect(780, 100, 125, 185), pygame.Rect(800, 550, 125, 185)]


#tan_0 = tank0(center=(t_w/2, t_y/2))
direction_0 = 'up'
direction_1 = 'down'
tank_speed = 3

# #game characters
# tank_size = 70

#movement variables
movement_speed = 0

#shell size
shell_size = 10
shells_0 = []
shells_1 = []

#shell speed
shell_speed = tank_speed + 2


def draw_tank1( tank, tank_img, tank_img_rotate, direction, keys, k_left, k_right, k_up, k_down):
    #tank copy left
    tank_copy_left = tank.copy()
    tank_copy_left.x -= tank_speed
    #tank copy right
    tank_copy_right = tank.copy()
    tank_copy_right.x += tank_speed
    #tank copy up
    tank_copy_up = tank.copy()
    tank_copy_up.y -= tank_speed
    #tank copy down
    tank_copy_down = tank.copy()
    tank_copy_down.y += tank_speed

    if keys[k_left] and tank.x > 0 and tank_copy_left.collidelist(walls) == -1:
        tank.x -= tank_speed
        tank_img_rotate = pygame.transform.rotate(tank_img, 90)
        direction = 'left'

    if keys[k_right] and tank.x < WIDTH and tank_copy_right.collidelist(walls) == -1:
        tank.x += tank_speed
        tank_img_rotate = pygame.transform.rotate(tank_img, -90)
        direction = 'right'

    if keys[k_up] and tank.y > 0 and tank_copy_up.collidelist(walls) == -1:
        tank.y -= tank_speed
        tank_img_rotate = pygame.transform.rotate(tank_img, 0)
        direction = 'up'

    if keys[k_down] and tank.y < HEIGHT - tank_size and tank_copy_down.collidelist(walls) == -1:
        tank.y += tank_speed
        direction = 'down'
        tank_img_rotate = pygame.transform.rotate(tank_img, 180)
     
    screen.blit(tank_img_rotate, tank)
    return tank, tank_img_rotate, direction

def draw_shells(shells):
    for shell in shells:
        pygame.draw.rect(screen, (255, 237, 0), shell[0])
        if shell[1] == 'left':
            shell[0].x -= shell_speed

        if shell[1] == 'right':
            shell[0].x += shell_speed
        
        if shell[1] == 'up':
            shell[0].y -= shell_speed

        if shell[1] == 'down':
            shell[0].y += shell_speed

        if shell[0].x > WIDTH or shell[0].y > HEIGHT or shell[0].x < 0 or shell[0].y < 0:
            shells.remove(shell)            
        
        if shell[0].collidelist(walls) != -1:
             shells.remove(shell)       

def new_shell(direction, tank):
    if direction == 'left':
       pygame.mixer.Sound.play(shot_sound)
       return pygame.Rect(tank.left - shell_size, tank.centery - (shell_size // 2), shell_size, shell_size), direction

    if direction == 'right':
       pygame.mixer.Sound.play(shot_sound)
       return pygame.Rect(tank.right - shell_size, tank.centery - (shell_size // 2), shell_size, shell_size), direction

    if direction == 'up':
       pygame.mixer.Sound.play(shot_sound)
       return pygame.Rect(tank.centerx - shell_size, tank.centery - (shell_size // 2), shell_size, shell_size), direction

    if direction == 'down':
       pygame.mixer.Sound.play(shot_sound)
       return pygame.Rect(tank.centerx - shell_size, tank.centery - (shell_size // 2), shell_size, shell_size), direction
    
def shells_objects(shells):
    objects = []
    for shell in shells:
        objects.append(shell[0])
    return objects

def win_menu(tank_img):
    global tank_0, direction_0, shells_0, lives_0, tank_1, direction_1, shells_1, lives_1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill((0,0,0))
        #WINNER screen

        #menu text
        winner_text = font.render('Winner!', True, (240,248,255))
        screen.blit(winner_text, (300, 150))
        info_text = font2.render('Press ENTER to continue', True, (240,248,255))
        screen.blit(info_text, (200, 520))

        winner_tank_0 = pygame.image.load('photos/tank_1.png')
        winner_tank_scale_0 = pygame.transform.scale(tank_img, (tank_size_winner, tank_size_winner))
        position_center = WIDTH // 2 - tank_size_winner // 2, HEIGHT // 2 - tank_size_winner // 2
        screen.blit(winner_tank_scale_0, (position_center))
        pygame.mixer.Sound.play(menu_sound)

     
        pygame.display.update()
        FPS.tick(60)
    
def move():
    pass
           
def main():
    global tank_0, tank_img_rotate_0, direction_0, tank_1, tank_img_rotate_1, direction_1, lives_0, lives_1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and len(shells_0) < 4:
                    global shell_speed
                    shells_0.append(new_shell(direction_0, tank_0))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g and len(shells_1) < 4:
                    global shell_speed
                    shells_1.append(new_shell(direction_1, tank_1))
            
        if tank_0.collidelist(shells_objects(shells_1)) != -1:
            pygame.mixer.Sound.play(hit_sound)
            shells_1.pop(tank_0.collidelist(shells_objects(shells_1)))
            lives_0 -= 1
            
        if tank_1.collidelist(shells_objects(shells_0)) != -1:
            pygame.mixer.Sound.play(hit_sound)
            shells_0.pop(tank_1.collidelist(shells_objects(shells_0)))
            lives_1 -= 1   

        screen.blit(rand_img, (0,0))  

        #tank_0 lives
        if lives_0 == 4:
            screen.blit(heart_scale_0, (660, 10))
            screen.blit(heart_scale_0, (625, 10))
            screen.blit(heart_scale_0, (590, 10))
            screen.blit(heart_scale_0, (555, 10))

        if lives_0 == 3:
            screen.blit(heart_scale_0, (660, 10))
            screen.blit(heart_scale_0, (625, 10))
            screen.blit(heart_scale_0, (590, 10))

        if lives_0 == 2:
            screen.blit(heart_scale_0, (660, 10))
            screen.blit(heart_scale_0, (625, 10))

        if lives_0 == 1:
            screen.blit(heart_scale_0, (660, 10))

        #tank_1 lives
        if lives_1 == 3:
            screen.blit(heart_scale_1, (10, 10))
            screen.blit(heart_scale_1, (45, 10))
            screen.blit(heart_scale_1, (80, 10))

        if lives_1 == 2:
            screen.blit(heart_scale_1, (10, 10))
            screen.blit(heart_scale_1, (45, 10))

        if lives_1 == 1:
            screen.blit(heart_scale_1, (45, 10))

        if lives_1 == 4:
            screen.blit(heart_scale_1, (10, 10))
            screen.blit(heart_scale_1, (45, 10))
            screen.blit(heart_scale_1, (80, 10))
            screen.blit(heart_scale_1, (115, 10))

        #tank and heart reinforcement collision
        if tank_0.colliderect(heart_c):
            pygame.mixer.Sound.play(select_sound)
            lives_0+=1
            heart_c.x = WIDTH + 100
        
        if tank_1.colliderect(heart_c):
            pygame.mixer.Sound.play(select_sound)
            lives_1+=1
            heart_c.x = WIDTH+100

        #tank menu images
        if lives_0 == 0:
            win_menu(tank_img_1)

        if lives_1 == 0:
            win_menu(tank_img_0)  

        #restart game after menu
        if event.type == pygame.K_KP_ENTER and win_menu:
            main()     
        
        for i in walls:
            pygame.draw.rect(screen, (240,248,255), i)
        
        keys = pygame.key.get_pressed()
        draw_shells(shells_0 )
        draw_shells(shells_1)

        tank_0, tank_img_rotate_0, direction_0 = draw_tank1(tank_0, tank_img_0, tank_img_rotate_0, direction_0, keys,
                                                            pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
        
        tank_1, tank_img_rotate_1, direction_1 = draw_tank1(tank_1, tank_img_1, tank_img_rotate_1, direction_1, keys,
                                                            pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)

        screen.blit(heart_img_bonus, heart_c) 
        pygame.display.update()
        FPS.tick(60)
main()



        
