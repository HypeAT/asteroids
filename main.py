import pygame
import constants
import player
from logger import log_state


def main():
    pygame.init()
    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2
    main_screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    triangle = player.Player(x, y)
    clock = pygame.time.Clock()

    while True:
        dt = clock.tick(60) / 1000
        main_screen.fill("black")
        triangle.update(dt)
        triangle.draw(main_screen)
        pygame.display.flip()
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()
