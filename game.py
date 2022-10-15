import resource
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Run and Jump Simulator')
clock = pygame.time.Clock()

test_font = pygame.font.Font('resources/font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('resources/graphics/Sky.png').convert()
ground_surface = pygame.image.load('resources/graphics/ground.png').convert()
text_surface = test_font.render('Run and Jump Simulator', False, 'Black' )
player_surface = pygame.image.load('resources/graphics/Player/player_walk_1.png').convert_alpha()
snail_surface = pygame.image.load('resources/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft = (800, 300))
player_rect = player_surface.get_rect(bottomleft = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos

    screen.blit(sky_surface, (0,0))        
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (210,50))
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)
   
    # if player_rect.colliderect(snail_rect):
    #    print("collisson")

    #mouse_pos = pygame.mouse.get_pos()
    #is_mouse_pressed = pygame.mouse.get_pressed()

    #if player_rect.collidepoint(mouse_pos) and is_mouse_pressed == (True, False, False):
     #   print("ouch! you clicked on me!")

    # mouse_pos = pygame.mouse.get_pos()

    if player_rect.collidepoint(mouse_pos):
       print("ouch! you hovered over me!")

    pygame.display.update()
    player_rect.left += 1
    snail_rect.left = snail_rect.left - 5

    if snail_rect.right < 0: 
        snail_rect.left = 800

    clock.tick(60)