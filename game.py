import resource
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Run and Jump Simulator')
clock = pygame.time.Clock()

test_font = pygame.font.Font('resources/font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('resources/graphics/Sky.png')
ground_surface = pygame.image.load('resources/graphics/ground.png')
text_surface = test_font.render('Run and Jump Simulator', False, 'Black' )
snail_surface = pygame.image.load('resources/graphics/snail/snail1.png')
snail_x_pos = 800

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (210,50))
    screen.blit(snail_surface, (snail_x_pos, 265))
    pygame.display.update()

    snail_x_pos = snail_x_pos - 4

    if snail_x_pos == -72:
        snail_x_pos = 800

    clock.tick(60)