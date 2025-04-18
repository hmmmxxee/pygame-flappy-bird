import pygame
import sys
import random
from sprites.platforms import Platforms
from sprites.doodle import Doodle
from sprites.springs import Spring
from sprites.game import Score, GameOver

pygame.init()
 
# Константы/Constants
WIDTH = 800
HEIGHT = 600
FPS = 60
 
# Создание окна/Window creating
screen = pygame.display.set_mode((WIDTH, HEIGHT))
surface = pygame.display.get_surface()
pygame.display.set_caption("Doodle Jump")
clock = pygame.time.Clock()
 
def main():
    # Спрайты/Sprites
    platforms = pygame.sprite.Group()
    for y in range(25, screen.get_height(), 50):
        x = random.randint(100,screen.get_width() -100)
        platforms.add(Platforms((x,y)))
    quantity = len(platforms)
    player = Doodle()
    springs = pygame.sprite.Group()
    score = Score()
    
    offset = 0
    game_over=False
    running = True
    while running:
        # Частота обновления экрана/Screen refresh rate
        clock.tick(FPS)
    
        # События/Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main()
        for platform in platforms:
            if (platform.rect.collidepoint(player.rect.bottomleft) or \
                platform.rect.collidepoint(player.rect.bottomright)) and player.gravity <= 0:
                if platform.color =='red':
                    platform.image = platform.broken
                else:
                    player.gravity = 15
        for spring in springs:
            if spring.rect.collidepoint(player.rect.bottomleft) or \
            spring.rect.collidepoint(player.rect.bottomright) or \
            spring.rect.collidepoint(player.rect.midbottom):
                if spring.image is not spring.relaxed:
                    spring.image = spring.relaxed
                    player.gravity = 50
        if player.rect.bottom < 0:
            offset = 20
        elif player.rect.bottom < screen.get_height() / 2:
            offset = 10
        else:
            offset = 0
        if player.rect.y > surface.get_height():
            end=GameOver()
            game_over =True

    
        # Рендеринг/Rendering
        screen.fill((255, 255, 255))
        for x in range(0, screen.get_width(), 10):
            pygame.draw.line(screen, (222,222,222), (x,0),(x, screen.get_height()))
        for i in range(0, screen.get_height(), 10):
            pygame.draw.line(screen, (222,222,222), (0,i),(screen.get_width(), i))
        platforms.draw(screen)
        player.draw(screen)
        springs.draw(screen)
        score.draw(screen)
        if game_over:
            end.draw(screen)

    
        # Обновление спрайтов/Updating sprites
        if not game_over:
            platforms.update(offset)
            player.update(offset)
            springs.update(offset)
            score.update(offset)
            if quantity > len(platforms):
                x = random.randint(100, screen.get_width() - 100)
                platform = Platforms((x, 0))
                platforms.add(platform)
                if platform.color == 'green' and random.randint(1,100) in range (1,10):
                    springs.add(Spring(platform.rect.topleft))
        
    
        # Обновление экрана/Screen Refresh
        pygame.display.update()
 
if __name__ == "__main__":
    main()
