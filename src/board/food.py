# import core modules and community packages
import pygame

class Food():
    def __init__(self, pos, color=(222, 161, 133)):
        # binding
        self.pos = pos
        self.color = color

    def draw(self, surface):
        x = self.pos[0]
        y = self.pos[1]

        pygame.draw.circle(surface, self.color, (x, y), 3)
