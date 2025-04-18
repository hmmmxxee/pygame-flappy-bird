import pygame
import random

class Platforms(pygame.sprite.Sprite):
    def __init__(self, coordinates):
        super().__init__()
        if random.randint(1,100) in range (1,11):
            self.image = pygame.image.load(r'C:\Users\49177\Desktop\python files\pygame-doodle.jump\assets\images\blue.png')
            self.color = 'blue'
        elif random.randint(1,100) in range (1,11):
            self.image = pygame.image.load(r'C:\Users\49177\Desktop\python files\pygame-doodle.jump\assets\images\red.png')
            self.broken = pygame.image.load(r'C:\Users\49177\Desktop\python files\pygame-doodle.jump\assets\images\red_1.png')
            self.color = 'red'
        else:
            self.image = pygame.image.load(r'C:\Users\49177\Desktop\python files\pygame-doodle.jump\assets\images\green.png')
            self.color = 'green'
        self.rect = self.image.get_rect()
        self.rect.center = coordinates
        self.step = 5
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def update(self, offset):
        self.rect.y += offset
        surface = pygame.display.get_surface()
        if self.rect.y > surface.get_height():
            self.kill()
        if self.color =='blue':
            self.rect.x += self.step
            if self.rect.centerx > surface.get_width() - 50 or self.rect.centerx < 50:
                self.step *= -1

        