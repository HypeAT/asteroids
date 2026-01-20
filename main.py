import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import player
import sys

from logger import log_state
from logger import log_event
from asteroids import Asteroid
from asteroidfield import AsteroidField
import shot


def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    pygame.init()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    main_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player.Player.containers = (updatable, drawable)
    shot.Shot.containers = (shots, drawable, updatable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    AsteroidField()
    player_1 = player.Player(x, y)
    clock = pygame.time.Clock()

    while True:
        dt = clock.tick(60) / 1000
        main_screen.fill("black")
        updatable.update(dt)
        for meteor in asteroids:
            if player_1.collides_with(meteor):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for bullet in shots:
            for target in asteroids:
                if bullet.collides_with(target):
                    bullet.kill()
                    target.split()
                    log_event("asteroid_shot")
        for drawing in drawable:
            drawing.draw(main_screen)
        pygame.display.flip()
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()
