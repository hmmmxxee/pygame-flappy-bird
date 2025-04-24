from typing import Any
import pygame

class City(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\49177\Desktop\python files\pygame-flappy-bird\assets\images\city.png')
        self.rect=self.image.get_rect()
        surface=pygame.display.get_surface()
        self.rect.center=surface.get_rect().center
    def draw(self,surface):
        surface.blit(self.image,self.rect)


class Road(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\49177\Desktop\python files\pygame-flappy-bird\assets\images\road.png')
        self.image1 = pygame.image.load(r'C:\Users\49177\Desktop\python files\pygame-flappy-bird\assets\images\road.png')
        self.rect=self.image.get_rect()
        self.rect1=self.image1.get_rect()
        surface=pygame.display.get_surface()
        self.rect.midleft = surface.get_rect().midleft
        self.rect1.midleft = self.rect.midright
        self.rect.bottomright=(288, 512)
        self.rect1.bottomleft=(288,512)
        self.rect.y+=25
        self.rect1.y+=25
    def draw(self,surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.image1, self.rect1)
    def update(self):
        self.rect.x-=2
        self.rect1.x-=2
        if self.rect.right < 0:
            self.rect.midleft = self.rect1.midright
        elif self.rect1.right < 0:
            self.rect1.midleft = self.rect.midright
        
