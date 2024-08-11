import pygame
import main
from wall import  walls

pygame.init()



#Wall(x350, y250, Ш200, В400)

'''----------start----------'''
# Завантаження фонового зображення
background_image = pygame.image.load('background.png')  # Замість 'background.jfif' вкажіть шлях до вашого зображення фону
background_image = pygame.transform.scale(background_image, (800, 500)) # задання розмірів фонового зображення
'''-----------end-----------'''

window = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
player = main.Player((400,250))
game = True
white = (255, 255, 255)
black = (0, 0, 0)



while game:
    window.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    player.events(event)
    window.blit(background_image, (0, 0))
    window.blit(player.image, player.rect)
    for w in walls:
        w.draw(window)
    clock.tick(30)
    pygame.display.update()


