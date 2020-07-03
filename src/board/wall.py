import pygame

class Wall():
    def __init__(self, pos, color=(33,33,222)):
        # binding
        self.pos = pos
        self.color = color

        # props
        self.dimensions = 16,16

    def draw(self, surface):
        x = self.pos[0]
        y = self.pos[1]

        w = self.dimensions[0]
        h = self.dimensions[1]

        pygame.draw.rect(surface, self.color, (x+2, y+2, w, h), 1)
