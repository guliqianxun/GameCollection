import pygame
from sys import exit
from random import randint, choice

Body_status = enumerate([['jump','work']])

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('assets/sprites/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('assets/sprites/player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1,player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('assets/sprites/player/jump.png').convert_alpha()
        self.body_status = 0

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 10

        self.jump_sound = pygame.mixer.Sound('assets/audio/jump.mp3')
        self.jump_sound.set_volume(0.5)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.body_status == 0:
            self.gravity = -5
            self.jump_sound.play()
        if keys[pygame.K_a]:
            self.rect.x -= 2
        if keys[pygame.K_d]:
            self.rect.x += 2

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300: 
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Under 500')
clock = pygame.time.Clock()
font = pygame.font.Font('assets/font/Pixeltype.ttf',50)

sky_surf = pygame.image.load('assets/sprites/Sky.png').convert()
ground_surf = pygame.image.load('assets/sprites/Ground.png').convert()

score_surf = font.render('My game', False, (64,64,64))
score_rect = score_surf.get_rect(center = (400,50))

snail_surf = pygame.image.load('assets/sprites/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600,300))

player_surf = pygame.image.load('assets/sprites/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surf,(0,0))
    screen.blit(ground_surf,(0,300))
    screen.blit(score_surf,score_rect)

    snail_rect.x -= 1
    if snail_rect.right < 0:
        snail_rect.left = 800
    player.update()
    screen.blit(player.image,player.rect)
    # screen.blit(snail_surf,snail_rect)
    # screen.blit(player_surf,player_rect)
    pygame.display.update()
    clock.tick(60)
