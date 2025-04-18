import pygame

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.step = 0
        self.points = 0
        self.font = pygame.font.Font(r'C:\Users\49177\Desktop\python files\pygame-doodle.jump\assets\fonts\gamefont.ttf', 20)
        self.image = self.font.render(f'{self.points}', True, (83,83,83))
        self.rect = self.image.get_rect()
        self.rect.topleft=(20,20)
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.image = self.font.render(f'{self.points}', True, (83,83,83))
    def update(self, offset):
        self.step += offset
        if self.step % 10 == 0:
            self.points += 1


class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(r'C:\Users\49177\Desktop\python files\pygame-doodle.jump\assets\fonts\gamefont.ttf', 20)
        self.image = self.font.render(f'G A M E  O V E R', (83,83,83),(0,0,0))
        self.rect = self.image.get_rect()
        surface = pygame.display.get_surface()
        self.rect.center=surface.get_rect().center
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
