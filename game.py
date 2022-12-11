from curses import KEY_A1, KEY_BACKSPACE
import resource
from time import sleep
from turtle import title
import pygame
from sys import exit
def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score2_surface = test_font.render(f'{round(current_time / 1000)}', False,(64,64,64))
    score2_rect = score2_surface.get_rect(topright = display_rect.topright)
    screen.blit(score2_surface,score2_rect)
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Run and Jump Simulator')
clock = pygame.time.Clock()
game_active = True
start_time = 0
display_rect = screen.get_rect(topleft = (0,0))

test_font = pygame.font.Font('resources/font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('resources/graphics/Sky.png').convert()
ground_surface = pygame.image.load('resources/graphics/ground.png').convert()
ground_rect = ground_surface.get_rect(bottomleft = (0,470))

player_surface = pygame.image.load('resources/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(bottomleft = (80, 300))
player_gravity = 0

snail_surface = pygame.image.load('resources/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft = (800, 300))

title_surface = test_font.render('Run and Jump Simulator', False, 'Black' )
title_rect = title_surface.get_rect(midtop = display_rect.midtop)

reset_surface = test_font.render('RESET PRESS R', False, (90, 20, 55))
reset_rect = reset_surface.get_rect(bottom = display_rect.bottom) 

score = 0
scored = False

game_over_surface = test_font.render('Game Over', False, (80,100,40))
game_over_rect = game_over_surface.get_rect(center = display_rect.center)

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     mouse_pos = event.pos

        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_SPACE: # and player_rect.bottom == ground_rect.top
            player_gravity -= 10 
           if event.key == pygame.K_r:
            if not game_active:
                start_time = pygame.time.get_ticks()
                score = 0
            game_active = True

        if event.type == pygame.KEYUP:
            # print("key up")
            player_gravity += 17

    if game_active:

        screen.blit(sky_surface, (0,0))        
        screen.blit(ground_surface, (0,300))
        screen.blit(title_surface, title_rect)
        screen.blit(snail_surface, snail_rect)
        screen.blit(player_surface, player_rect)

        score_surface = test_font.render('SCORE: ' + str(score), False, (80,200,40))
        score_rect = score_surface.get_rect(topleft = display_rect.topleft)

        pygame.draw.rect(screen, (90,5,100), score_rect)
        pygame.draw.rect(screen, (89,50,10), score_rect, 10)
        screen.blit(score_surface, score_rect)
        display_score()
        mouse_pos = pygame.mouse.get_pos()

        # if player_rect.collidepoint(mouse_pos):
        #     print("ouch! you hovered over me!")
        #player_rect.left += 1

        snail_rect.left = snail_rect.left - 5
        player_rect.top += player_gravity

        if snail_rect.colliderect(player_rect):
            print("snail x:" + str(snail_rect.x))
            print("player x:" + str(player_rect.x))
            game_active = False
            scored = False
        else:
            player_length, _ = player_rect.size

            if scored == False and abs(snail_rect.x - player_rect.x) < player_length:
                print("give a point..")
                scored = True

        if player_rect.colliderect(ground_rect):
            player_rect.bottom = ground_rect.top
            player_gravity = 0
            if scored:
                score = score + 1
                scored = False

        if player_rect.top < 110:
            player_gravity += 1

        if snail_rect.right < 0: 
            snail_rect.left = 800
        
    else:          
        screen.fill('Gray')
        pygame.draw.rect(screen, (90,5,100), game_over_rect)
        pygame.draw.rect(screen, (89,50,10), game_over_rect, 10)

        score_surface = test_font.render('FINAL SCORE: ' + str(score), False, (80,200,40))
        score_rect = score_surface.get_rect(topleft = display_rect.topleft)

        screen.blit(score_surface, score_rect)

        screen.blit(game_over_surface, game_over_rect)
        screen.blit(reset_surface, reset_rect)
        snail_rect.left = 800

    pygame.display.update()
    clock.tick(60)
