import pygame

class Wall:
    def __init__(self, x, y, width, height, color=(22, 26, 31)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

walls = [
    Wall(0, 0, 1, 500),
    Wall(800, 0, 800, 800),
    Wall(0, 500, 800, 800),
    Wall(0, 0, 800, 1)
    
    
]