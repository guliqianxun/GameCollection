import pygame
from sys import exit
from random import randint, choice

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surf,(0,0))
    screen.blit(ground_surf,(0,300))
    screen.blit(score_surf,score_rect)

    snail_rect.x -= 4
    if snail_rect.right < 0:
        snail_rect.left = 800

    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf,player_rect)
    
    pygame.display.update()
    clock.tick(60)
