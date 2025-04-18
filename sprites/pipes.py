import pygame
from random import randint

class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image1 = pygame.image.load(r'C:\Users\49177\Desktop\python files\pygame-flappy-bird\assets\images\pipe1.png')
        self.image2 = pygame.image.load(r'C:\Users\49177\Desktop\python files\pygame-flappy-bird\assets\images\pipe2.png')
        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()
        surface = pygame.display.get_surface()
        self.rect1.x = surface.get_rect().right
        self.rect1.y = randint(150, 350)
        self.rect2.x = self.rect1.x
        self.rect2.y = self.rect1.y - 450
    def draw(self, surface):
        surface.blit(self.image1, self.rect1)
        surface.blit(self.image2, self.rect2)
    def update(self):
        self.rect1.x -= 2 
        self.rect2.x -= 2
        surface = pygame.display.get_surface()
        if self.rect1.right < surface.get_rect().left:
            self.kill()
        if self.rect2.right < surface.get_rect().left:
            self.kill()