import pygame



class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.font = pygame.font.Font(r'C:\Users\49177\Desktop\python files\pygame-flappy-bird\assets\fonts\gamefont.ttf')
        self.image = self.font.render(f'{self.points}', True, (255,255,255))
        self.sound_score = pygame.mixer.Sound(r'C:\Users\49177\Desktop\python files\pygame-flappy-bird\assets\sounds\point.wav')
        self.rect = self.image.get_rect()
        surface=pygame.display.get_surface()
        self.rect.center = surface.get_rect().center
        self.rect.y = 70
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.image = self.font.render(f'{self.points}', True, (255,255,255))