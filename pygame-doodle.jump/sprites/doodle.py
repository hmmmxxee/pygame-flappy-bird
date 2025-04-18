import pygame

class Doodle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.left = pygame.image.load(r'C:\Users\49177\Desktop\python files\pygame-doodle.jump\assets\images\left.png')
        self.left_1 = pygame.image.load(r'C:\Users\49177\Desktop\python files\pygame-doodle.jump\assets\images\left_1.png')
        self.right = pygame.transform.flip(self.left, True, False)
        self.right_1 = pygame.transform.flip(self.left_1, True, False)
        self.image = self.left
        self.rect = self.image.get_rect()
        self.gravity = 0
        surface = pygame.display.get_surface()
        self.rect.center = surface.get_rect().center
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def update(self, offset):
        self.rect.y += offset
        surface = pygame.display.get_surface()
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.rect.x -= 10
            self.image = self.left
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.rect.x += 10
            self.image = self.right
        if self.rect.x > surface.get_width() + 20:
            self.rect.x = -80
        if self.rect.x < -80:
            self.rect.x = 800
        self.rect.y -= self.gravity
        self.gravity -=1
        if self.gravity == 0 and self.image == self.left:
            self.image = self.left_1
        if self.gravity >= 0 and self.image == self.right:
            self.image = self.right_1
        if self.gravity < 0 and self.image == self.left_1:
            self.image = self.left
        if self.gravity < 0 and self.image == self.right_1:
            self.image = self.right