import pygame
import constants
import player
from logger import log_state

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

def main():
    pygame.init()
    pygame.time.Clock()
    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2
    main_screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    triangle = player.Player(x, y)

    while True:
        dt = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            log_state()
            main_screen.fill("black")
            triangle.draw(main_screen)
            pygame.display.flip()
            clock.tick(60)
            dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
