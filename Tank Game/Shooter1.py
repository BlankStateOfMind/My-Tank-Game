import pygame

pygame.init()

WIDTH, HEIGH = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGH))
pygame.display.set_caption('Hello World')

#set frame rate
clock = pygame.time.Clock()
FPS = 60

#define colours
BG = (144, 201, 120)

def draw_bg():
    screen.fill(BG)

#define player action variables
moving_left = False
moving_right = False

class Soldier(pygame.sprite.Sprite):
    def init(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.init(self)
        self.char_type = char_type
        self.speed = speed   
        self.direction = 1
        self.animation_list = []
        self.index = 0
        for i in range(5):
            img = pygame.image.load(f'Photos/0{i}.png')
            img = self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale))) 
        self.image = self.animation [self.index]
        self.animation_list.append(img) 
        self.flip = False
        self.rect = img.get_rect()
        self.rect.center = (x, y)

    def move(self, moving_left, moving_right):
        #reset movement variables
        dx = 0
        dy = 0

        #assign movement variables
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1

        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy


    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


player = Soldier('player', 200, 200, 3, 5)
enemy = Soldier('enemy', 400, 200, 3, 5)

run = True
while run:

    clock.tick(FPS)

    draw_bg()

    player.draw()
    enemy.draw()

    player.move(moving_left, moving_right)

    #quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        
        #keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_ESCAPE:
                run = False


        #keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False


    pygame.display.update()

pygame.quit()