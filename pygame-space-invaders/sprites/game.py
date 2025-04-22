import pygame

class Game(pygame.sprite.Sprite):
    def __init__(self, phrase):
        super().__init__()
        self.font=pygame.font.Font(r'C:\Users\49177\Desktop\python files\pygame-space-invaders\assets\fonts\gamefont.ttf')
        self.image=self.font.render(phrase, (255,255,255),(255,255,255))
        self.rect=self.image.get_rect()
        surface=pygame.display.get_surface()
        self.rect.center=surface.get_rect().center
    def draw(self, surface):
        surface.blit(self.image, self.rect)
