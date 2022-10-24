import resource
from turtle import title
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Run and Jump Simulator')
clock = pygame.time.Clock()

display_rect = screen.get_rect(topleft = (0,0))

test_font = pygame.font.Font('resources/font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('resources/graphics/Sky.png').convert()
ground_surface = pygame.image.load('resources/graphics/ground.png').convert()

player_surface = pygame.image.load('resources/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(bottomleft = (80, 300))

snail_surface = pygame.image.load('resources/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft = (800, 300))

title_surface = test_font.render('Run and Jump Simulator', False, 'Black' )
title_rect = title_surface.get_rect(midtop = display_rect.midtop)

score_surface = test_font.render('SCORE: ', False, 'Black' )
score_rect = score_surface.get_rect(center = display_rect.center)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
    screen.blit(sky_surface, (0,0))        
    screen.blit(ground_surface, (0,300))
    screen.blit(title_surface, title_rect)
    screen.blit(score_surface, score_rect)
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)
   
    #pygame.draw.line(screen, 'Pink', display_rect.topleft, display_rect.bottomright, 10)
    pygame.draw.line(screen, 'Gold', snail_rect.topleft, pygame.mouse.get_pos(),10)


    # if player_rect.colliderect(snail_rect):
    #    print("collisson")

    #mouse_pos = pygame.mouse.get_pos()
    #is_mouse_pressed = pygame.mouse.get_pressed()

    #if player_rect.collidepoint(mouse_pos) and is_mouse_pressed == (True, False, False):
     #   print("ouch! you clicked on me!")

    mouse_pos = pygame.mouse.get_pos()

    if player_rect.collidepoint(mouse_pos):
       print("ouch! you hovered over me!")

    pygame.display.update()
    player_rect.left += 1
    snail_rect.left = snail_rect.left - 5

    if snail_rect.right < 0: 
        snail_rect.left = 800

    clock.tick(60)