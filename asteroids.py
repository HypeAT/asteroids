from circleshape import CircleShape
import pygame
import constants
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            rot_1 = self.velocity.rotate(angle) * 1.2
            rot_2 = self.velocity.rotate(-angle) * 1.2
            new_rad = self.radius - constants.ASTEROID_MIN_RADIUS
            ast_1 = Asteroid(self.position.x, self.position.y, new_rad)
            ast_2 = Asteroid(self.position.x, self.position.y, new_rad)
            ast_1.velocity = rot_1
            ast_2.velocity = rot_2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt