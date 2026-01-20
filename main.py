import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import player
from logger import log_state


def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    pygame.init()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    main_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player.Player.containers = (updatable, drawable)
    player.Player(x, y)
    clock = pygame.time.Clock()

    while True:
        dt = clock.tick(60) / 1000
        main_screen.fill("black")
        updatable.update(dt)
        for drawing in drawable:
            drawing.draw(main_screen)
        pygame.display.flip()
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()
