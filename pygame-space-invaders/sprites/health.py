import pygame

class Healthbar(pygame.sprite.Sprite):
    def __init__(self, health):
        super().__init__()
        self.hearts=[]
        surface=pygame.display.get_surface()
        for i in range(health):
            self.image = pygame.image.load(r'C:\Users\49177\Desktop\python files\pygame-space-invaders\assets\images\heart.png')
            self.rect = self.image.get_rect()
            self.rect.topright=(surface.get_width() -10 - i * 35, 10)
            self.hearts.append((self.image, self.rect))
    def draw(self, surface):
        surface.blits(self.hearts)
