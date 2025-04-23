import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, coordinates):
        super().__init__()
        self.images=[r'C:\Users\49177\Desktop\python files\pygame-space-invaders\assets\images\exp{}.png'.format(i) for i in range(1,6)]
        self.index=0
        self.image=pygame.image.load(self.images[self.index])
        self.rect=self.image.get_rect()
        self.rect.center=coordinates
        self.sound=pygame.mixer.Sound(r'C:\Users\49177\Desktop\python files\pygame-space-invaders\assets\sounds\explosion.wav')
        self.sound.set_volume(0.1)
        self.step=0
    def draw(self,surface):
        surface.blit(self.image, self.rect)
    def update(self):
        self.index += 1
        self.step += 1
        if self.step % 3 == 0:
            self.image = pygame.image.load(self.images[self.index])
        if self.index >= len(self.images) -1:
            self.kill()
