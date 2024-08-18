import pygame
import main

from wall import walls
from chest_ import Chest_1

pygame.init()

'''----------start----------'''
# Завантаження фонового зображення
background_image = pygame.image.load('background.png')  # Замість 'background.jfif' вкажіть шлях до вашого зображення фону
background_image = pygame.transform.scale(background_image, (800, 500)) # задання розмірів фонового зображення
'''-----------end-----------'''

window = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
player = main.Player((400, 250))
game = True
white = (255, 255, 255)
black = (0, 0, 0)
chest_1 = Chest_1(100, 100, 50, 40, 'chest_1.png')

while game:
    window.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    player.events(event)
    
    # Check for collision between player and chest
    if player.rect.colliderect(chest_1.rect):
        chest_1.change_image('chest_2.png')
    
    window.blit(background_image, (0, 0))
    window.blit(player.image, player.rect)
    window.blit(chest_1.image, (chest_1.rect.x, chest_1.rect.y))  
    for w in walls:
        w.draw(window)
    
    clock.tick(30)
    pygame.display.update()
