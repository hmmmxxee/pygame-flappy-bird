import pygame
import sys
from sprites.space import Space
from sprites.spaceship import Spaceship
from sprites.alien import Alien, generate_aliens
from sprites.explosion import Explosion
from sprites.health import Healthbar
from sprites.game import Game


pygame.init()
 
# Константы
WIDTH = 600
HEIGHT = 700
FPS = 60
 
# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()
 
def main():
    # Спрайты
    space=Space()
    player_bullets=pygame.sprite.Group()                     
    player=Spaceship(player_bullets)
    players=pygame.sprite.GroupSingle()
    players.add(player)
    aliens = pygame.sprite.Group()
    alien_bullets = pygame.sprite.Group()
    generate_aliens(aliens, alien_bullets)
    explosions=pygame.sprite.Group()
    healthbar=Healthbar(player.health)
    game=pygame.sprite.GroupSingle()


    running = True
    while running:
        # Частота обновления экрана
        clock.tick(FPS)
    
        # События
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for alien in aliens.sprites():
            if pygame.sprite.spritecollide(alien, player_bullets, True, pygame.sprite.collide_mask):
                explosion=Explosion(alien.rect.center)
                explosion.sound.play()
                explosions.add(explosion)
                alien.kill() 
        for player in players.sprites(): 
            if pygame.sprite.spritecollide(player, alien_bullets, True, pygame.sprite.collide_mask):
                player.health -= 1
                healthbar.hearts.pop()
                if player.health < 1:
                    explosion = Explosion(player.rect.center)
                    explosion.sound.play()
                    explosions.add(explosion)
                    player.kill()
                else:
                    player.sound_damage.play()
        if not aliens.sprites():
            game.add(Game('Y O U  W I N !'))
            key=pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                main()
        elif not players.sprites():
            game.add(Game('G A M E  O V E R'))
            key=pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                main()
        
        # Рендеринг
        screen.fill((0, 0, 0))
        space.draw(screen)
        players.draw(screen)
        player_bullets.draw(screen)
        aliens.draw(screen)
        explosions.draw(screen)
        alien_bullets.draw(screen)
        healthbar.draw(screen)
        game.draw(screen)

        # Обновление спрайтов
        players.update()
        player_bullets.update()
        explosions.update()
        aliens.update()
        alien_bullets.update()

    
        # Обновление экрана
        pygame.display.update()
        space.update()
 
if __name__ == "__main__":
    main()


