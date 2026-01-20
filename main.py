import pygame
import constants
from logger import log_state
def main():
    pygame.init()
    pygame.time.Clock()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    while True:
        dt = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            log_state()
            screen.fill("black")
            pygame.display.flip()
            clock.tick(60)
            dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
