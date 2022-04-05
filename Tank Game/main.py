from tkinter import CENTER
from turtle import width
import time
import pygame
import random
import sys

pygame.init()

WIDTH = 540
HEIGHT = 700
x = WIDTH
y = HEIGHT
win = pygame.display.set_mode((WIDTH, HEIGHT)) 
record = 0
with open('record.txt', 'r') as record_file:
    record = int(record_file.read())

#game background
bg_img = pygame.image.load('bg.jpg')
sky_img = pygame.image.load('bg_sea.jpg')
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))
sky_img = pygame.transform.scale(sky_img, (WIDTH, HEIGHT))
rand_bg = random.choice([bg_img, sky_img])


icon = pygame.image.load('cola.png')
pygame.display.set_icon(icon)

container_w = 60
container_y = 60
#container_speed = 20
container_img = pygame.image.load('container.png')
container_img = pygame.transform.scale(container_img, (container_w, container_y))
cont = container_img.get_rect(center=(WIDTH/1, HEIGHT-70))

heart_w = 30
heart_y = 30
heart_img = pygame.image.load('heart.png')
heart_img = pygame.transform.scale(heart_img, (heart_w, heart_y))

cola_w = 70
cola_y = 70
cola_speed = 4
#cola_size = 500

falling_heart_images = pygame.image.load('heart.png')
cola_images = pygame.image.load('cola.png')
cola_images1 = pygame.image.load('cola_1.png')
cola_images2 = pygame.image.load('cola_can.png')
ketchup_images = pygame.image.load('ketchup.png')

cola_img = pygame.transform.scale(cola_images, (cola_w, cola_y))
cola_img1 = pygame.transform.scale(cola_images1, (cola_w, cola_y))
cola_img2 = pygame.transform.scale(cola_images2, (cola_w, cola_y))
ketchup_img = pygame.transform.scale(ketchup_images, (cola_w, cola_y))
falling_heart_scale = pygame.transform.scale(falling_heart_images, (cola_w, cola_y))


#sound effects
damage_sound = pygame.mixer.Sound('sounds/damage_sound_edited.wav')
game_over_sound = pygame.mixer.Sound('sounds/game_over_sound2.wav')
game_started_sound = pygame.mixer.Sound('sounds/game_started_sound.wav')
score_sound = pygame.mixer.Sound('sounds/score_sound.wav')
pygame.mixer.music.set_volume(0.01)
pygame.mixer.Sound.play(game_over_sound)

clock = pygame.time.Clock()
FPS = 60

#define player action variables

pygame.display.set_caption('Falling Coca Cola')

image = pygame.image.load('photos/container.png')

#class Player(pygame.sprite.Sprite):

font = pygame.font.Font('Lato-Bold.ttf', 20)
font_menu_title = pygame.font.Font('Lato-Bold.ttf', 45)
font_menu = pygame.font.Font('Lato-Bold.ttf', 30)
upgrade_font =  pygame.font.Font('Lato-Bold.ttf', 150)

#movement function
def move(self, moving_left, moving_right):
        #reset movement variables
        dx = 0
        dy = 0

        #assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
        if moving_right:
            dx = self.speed

        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy

#container_box = container_img.get_rect()
colas = []
def new_cola(colas):
    if len(colas) == 0:
        cola_x = random.randint(0, WIDTH - cola_w)
        cola_y1 = random.randint(-500, -200)
        coke = pygame.Rect(cola_x, cola_y1, cola_w, cola_y)
        colas.append(coke)
    return colas
colas = new_cola(colas)

cola_cans = []
def new_cola_cans(cola_cans):
    if len(cola_cans) == 0:
        cola_x = random.randint(0, WIDTH - cola_w)
        coke_cans = pygame.Rect(cola_x, -20, cola_w, cola_y)
        cola_cans.append(coke_cans)
    return cola_cans
cola_cans = new_cola(cola_cans)

ketchups = []
def new_ketchups(ketchups):
    if len(ketchups) == 0:
        ketchup_x = random.randint(0, WIDTH - cola_w)
        ketchup = pygame.Rect(ketchup_x, -10, cola_w, cola_y)
        ketchups.append(ketchup)
    return ketchups
ketchups = new_ketchups(ketchups)

score = 0
lives = 3
x = 50
y = 50
radius = 40
run = True

def draw_menu():
    global score, lives, colas, level_up1, cola_speed, cola_cans
    while True:
        for event in pygame.event.get():
            #quit game
            if event.type == pygame.QUIT:
                pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            lives = 3
            colas = []
            colas = new_cola(colas)
            level_up1 = 5
            cola_speed = 4
            score = 0
            break
        
        display_surface = pygame.Surface((250, 50))#Its width and height
        display_surface.fill((169,169,169))
        win.blit(display_surface,(140, 385))#Its position on screen

        game_over = font_menu_title.render('GAME OVER!', True, (205,51,51))
        start_over = font_menu.render('RESTART GAME', True, (0,0,0))
        final_score = font_menu.render('YOUR SCORE: ' + str(score), True, (0,100,0))
        record_score = font_menu.render('RECORD SCORE: ' + str(record), True, (238,173,14))
        win.blit(game_over, (140,200))
        win.blit(start_over, (150,390))
        win.blit(final_score, (150,320))
        win.blit(record_score, (150,270))
        clock.tick(FPS)
        pygame.display.update()

def start_menu():
    draw_menu()

def paused():
    paused = True
    while paused: 
       menu_btn = font.render('Paused', True, (245,245,220))
 
level_up1 = 15
def main():
    global level_up1, cola_speed, score, lives, colas, cola_cans, ketchups, record

    while True:   
        for event in pygame.event.get():
            #quit game
            if event.type == pygame.QUIT:
                pygame.quit()

        if score >= level_up1:
            level_up1 += 10
            cola_speed += 2
        if score >= level_up1 and lives == 1:
            win.blit(heart_img, (465,20))
        if level_up1 == 30:
            level_up1 += 10
            cola_speed += 4

        win.blit(rand_bg, (0,0))
        text = font.render('Score:' + str(score), True, (245,245,220))
        score_text1 = font.render('Hello', True, (245,245,220))

        if lives == 3:
            win.blit(heart_img, (500,20))
            win.blit(heart_img, (465,20))
            win.blit(heart_img, (430,20))
        elif lives == 2:
            win.blit(heart_img, (500,20))
            win.blit(heart_img, (465,20))
        elif lives == 1:
            win.blit(heart_img, (500,20))
        elif lives <= 0:
            if score > record:
                record = score
            draw_menu()

        if score == 1:
            win.blit(score_text1, (250, 300))
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and cont.x > 0:
            cont.x -= 7
        if keys[pygame.K_d] and cont.x < WIDTH - container_w:
            cont.x += 7
        #exiting game
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        #displays images   
        win.blit(container_img, cont)
        win.blit(text, (20, 20))
        # win.blit(menu_btn, (100, 200))

        for cola in colas:
            cola.y += cola_speed
            win.blit(cola_img, cola)
            if cont.colliderect(cola):
                score += 1
                m = pygame.mixer.Sound.play(score_sound)
                m.set_volume(0.2)
                colas.remove(cola)
                colas = new_cola(colas) 
            if cola.y > HEIGHT:
                lives -= 1
                t = pygame.mixer.Sound.play(damage_sound)
                t.set_volume(0.2)
                colas.remove(cola)
                colas = new_cola(colas)

        for cola2 in cola_cans:
            cola2.y += cola_speed
            win.blit(cola_img2, cola2)
            if cont.colliderect(cola2):
                score += 1
                m = pygame.mixer.Sound.play(score_sound)
                m.set_volume(0.2)
                cola_cans.remove(cola2)
                cola_cans = new_cola_cans(cola_cans) 
            if cola2.y > HEIGHT:
                lives -= 1
                t = pygame.mixer.Sound.play(damage_sound)
                t.set_volume(0.2)
                cola_cans.remove(cola2)
                cola_cans = new_cola_cans(cola_cans)

            for ketchup2 in ketchups:
                ketchup2.y += cola_speed
                win.blit(ketchup_img, ketchup2)
                if cont.colliderect(ketchup2):
                    score += 1
                    m = pygame.mixer.Sound.play(score_sound)
                    m.set_volume(0.2)
                    ketchups.remove(ketchup2)
                    ketchups = new_ketchups(ketchups) 
                if ketchup2.y > HEIGHT:
                    lives -= 1
                    t = pygame.mixer.Sound.play(damage_sound)
                    t.set_volume(0.2)
                    ketchups.remove(ketchup2)
                    ketchups = new_ketchups(ketchups)

        pygame.display.update()

        clock.tick(FPS)

if __name__ == '__main__':
    main()
