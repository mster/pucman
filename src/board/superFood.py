# import core modules and community packages
import pygame

class SuperFood():
    def __init__(self, pos, size, color=(222, 161, 133)):
        # binding
        self.pos = pos
        self.color = color
        self.radius = min(size) // 2

    def draw(self, surface):
        x = self.pos[0]
        y = self.pos[1]

        pygame.draw.circle(surface, self.color, (x, y), int(self.radius * 0.7))
