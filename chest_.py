import pygame

class Chest_1:
    def __init__(self, x, y, width, height, image):
        self.original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.original_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height

    def change_image(self, new_image):
        self.original_image = pygame.image.load(new_image)
        self.image = pygame.transform.scale(self.original_image, (self.width, self.height))
