from curses import KEY_A1, KEY_BACKSPACE
import pygame
from sys import exit
from random import randint
from datetime import datetime

def now():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score2_surface = test_font.render(f'{round(current_time / 1000)}', False,(64,64,64))
    score2_rect = score2_surface.get_rect(topright = display_rect.topright)
    screen.blit(score2_surface, score2_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > - snail_surface.get_width()]

        return obstacle_list

    else: return []

def collisions(player, obstacles):
    if obstacles:

        for obstacle in obstacles:
            if player.colliderect(obstacle):
                return False

    return True

def animate_player():
    global player_walk, player_index

    player_index += 0.1
    if player_index >= len(player_walk):
        player_index = 0

    if player_rect.bottom < 300:
        return player_jump
    else:
        return player_walk[int(player_index)]



pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Run and Jump Simulator')
clock = pygame.time.Clock()
game_active = False
start_time = 0
display_rect = screen.get_rect(topleft = (0,0))

test_font = pygame.font.Font('resources/font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('resources/graphics/Sky.png').convert()
ground_surface = pygame.image.load('resources/graphics/ground.png').convert()
ground_rect = ground_surface.get_rect(bottomleft = (0,470))

player_gravity = 0
floor = 300

player_walk_1 = pygame.image.load('resources/graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('resources/graphics/Player/player_walk_2.png').convert_alpha()
player_jump = pygame.image.load('resources/graphics/Player/jump.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_rect = player_walk_1.get_rect(midbottom = (80, floor))

player_stand = pygame.image.load('resources/graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400,200))

obstacle_rect_list = []

snail_frame1 = pygame.image.load('resources/graphics/snail/snail1.png').convert_alpha()
snail_frame2 = pygame.image.load('resources/graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame1, snail_frame2]
snail_index = 0
snail_surface = snail_frames[snail_index]
snail_rect = snail_surface.get_rect()

fly_frame1 = pygame.image.load('resources/graphics/Fly/Fly1.png').convert_alpha()
fly_frame2 = pygame.image.load('resources/graphics/Fly/Fly2.png').convert_alpha()
fly_frames = [fly_frame1, fly_frame2]
fly_index = 0
fly_surface = fly_frames[fly_index]

title_surface = test_font.render('Run and Jump Simulator', False, 'Black' ).convert_alpha()
title_surface = pygame.transform.smoothscale(title_surface, (300, 30))
title_rect = title_surface.get_rect(midtop = display_rect.midtop)

reset_surface = test_font.render('RESET PRESS R', False, (90, 20, 55))
reset_rect = reset_surface.get_rect(bottom = display_rect.bottom)

score = 0
scored = False

game_over_surface = test_font.render('Game Over', False, (80,100,40))
game_over_rect = game_over_surface.get_rect(center = display_rect.center)

add_obstacle_event = pygame.USEREVENT + 1
pygame.time.set_timer(add_obstacle_event, 1500)

snail_animation_event = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_event, 600)

fly_animation_event = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_event, 200)

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
                obstacle_rect_list = []
                print("cleared the list" + str(obstacle_rect_list))
            game_active = True

        if event.type == pygame.KEYUP:
            player_gravity += 17

        if game_active:

            if event.type == add_obstacle_event:
                if randint(0,2) == 0:
                    obstacle_rect_list.append(snail_surface.get_rect(bottomleft = (randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surface.get_rect(bottomleft = (randint(900, 1100), 160)))

            if event.type == snail_animation_event:
                if snail_index == 0:
                    snail_index = 1
                else:
                    snail_index = 0
                snail_surface = snail_frames[snail_index]


            if event.type == fly_animation_event:
                if fly_index == 0:
                    fly_index = 1
                else:
                    fly_index = 0
                fly_surface = fly_frames[fly_index]


    if game_active:

        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))

        screen.blit(animate_player(),
                    player_rect)

        score_surface = test_font.render('SCORE: ' + str(score), False, (80,200,40))
        score_rect = score_surface.get_rect(topleft = display_rect.topleft)

        pygame.draw.rect(screen, (90,5,100), score_rect)
        pygame.draw.rect(screen, (89,50,10), score_rect, 10)
        screen.blit(score_surface, score_rect)

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        game_active = collisions(player_rect, obstacle_rect_list)

        display_score()

        mouse_pos = pygame.mouse.get_pos()

        player_rect.top += player_gravity

        if player_rect.colliderect(ground_rect):
            player_rect.bottom = ground_rect.top
            player_gravity = 0
            if scored:
                score = score + 1
                scored = False

        if player_rect.top < 110:
            player_gravity += 1

    else:
        screen.fill((94, 129, 152))

        score_surface = test_font.render('FINAL SCORE: ' + str(score), False, (80,200,40))
        score_rect = score_surface.get_rect(topleft = display_rect.topleft)

        if score > 0:
            screen.blit(score_surface, score_rect)

        screen.blit(reset_surface, reset_rect)

        screen.blit(title_surface, title_rect)
        screen.blit(player_stand, player_stand_rect)

    pygame.display.update()
    clock.tick(60)
