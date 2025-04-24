import pygame
import sys
from sprites.background import City
from sprites.background import Road
from sprites.bird import Bird
from sprites.pipes import Pipe
from sprites.game import Score

pygame.init()
 
# Константы/Constants
WIDTH = 288
HEIGHT = 512
FPS = 60
 
# Создание окна/Window creating
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
 
def main():
    # Спрайты/Sprites
    city = City()
    road = Road()
    player = Bird()
    pipes = pygame.sprite.Group()
    pipes.add(Pipe())
    score = Score()

    game_over = False
    checkpoint = False
    running = True
    while running:
        # Частота обновления экрана/Screen refresh rate
        clock.tick(FPS)
    
        # События/Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if pipes.sprites()[0].rect1.x < player.rect.x and not checkpoint:
            score.points += 1
            checkpoint = True
            score.sound_score.play()
        for pipe in pipes:
            if (pipe.rect1.collidepoint(player.rect.midbottom) or 
                pipe.rect2.collidepoint(player.rect.midtop)) and not game_over:
                game_over = True
                player.sound_die.play()                           
        if (player.rect.top > road.rect.top or player.rect.top < city.rect.top) and not game_over:
            game_over=True
            player.sound_die.play()
    
        # Рендеринг/Rendering
        city.draw(screen)
        for pipe in pipes:
            pipe.draw(screen)
        road.draw(screen)
        player.draw(screen)
        score.draw(screen)
        
    
        # Обновление спрайтов/Updating sprites
        if not game_over:
            road.update()
            player.update()
            pipes.update()
            if len(pipes) < 1:
                pipes.add(Pipe())
                checkpoint = False
    
        # Обновление экрана/Screen Refresh
        pygame.display.update()
 
if __name__ == "__main__":
    main()