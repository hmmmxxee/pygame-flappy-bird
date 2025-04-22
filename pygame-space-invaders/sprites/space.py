import pygame

class Space(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(r'C:\Users\49177\Desktop\python files\pygame-space-invaders\assets\images\space.png')
        self.image_1 = pygame.image.load(r'C:\Users\49177\Desktop\python files\pygame-space-invaders\assets\images\space.png')
        self.rect=self.image.get_rect()
        self.rect_1=self.image.get_rect()
        surface=pygame.display.get_surface()
        self.rect.midbottom =surface.get_rect().midbottom
        self.rect_1.midbottom=self.rect.midtop
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.image_1, self.rect_1)
    def update(self):
        surface=pygame.display.get_surface()
        self.rect.y += 1
        self.rect_1.y += 1
        if self.rect.y >= surface.get_height():
            self.rect.midbottom = self.rect_1.midtop
        if self.rect_1.y >= surface.get_height():
            self.rect_1.midbottom = self.rect.midtop