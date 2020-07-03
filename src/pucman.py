import pygame

class Pucman():
    def __init__(self, start, color=(255,255,0)):
        # print('I\'m PUCMAN!')

        # bind params
        self.pos = start

        # props
        self.dimensions = 20,20
        self.color = color
        self.dir = 0,0

    def draw(self, surface):
        x = self.pos[0] + self.dimensions[0]//2
        y = self.pos[1] + self.dimensions[1]//2

        w = self.dimensions[0]
        h = self.dimensions[1]
        radius = min(w//2,h//2)

        pygame.draw.circle(surface, self.color, (x, y), radius)

        # left
        if (self.dir == (-1, 0)): 
            pygame.draw.polygon(surface, (0,0,0), [
                (self.pos[0], self.pos[1]),
                (self.pos[0], self.pos[1] + self.dimensions[1]),
                (x,y)
            ])

        # up
        elif (self.dir == (0, -1)):
            pygame.draw.polygon(surface, (0,0,0), [
                (self.pos[0], self.pos[1]),
                (self.pos[0] + self.dimensions[0], self.pos[1]),
                (x,y)
            ])

        #down
        elif (self.dir == (0, 1)):
            pygame.draw.polygon(surface, (0,0,0), [
                (self.pos[0], self.pos[1] + self.dimensions[1]),
                (self.pos[0] + self.dimensions[0], self.pos[1] + self.dimensions[1]),
                (x,y)
            ])
            
        # right as default
        else: 
            pygame.draw.polygon(surface, (0,0,0), [
                (self.pos[0] + self.dimensions[0], self.pos[1]),
                (self.pos[0] + self.dimensions[0], self.pos[1] + self.dimensions[1]),
                (x,y)
            ])

        
    def move(self, board):
        # check for QUIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # check KEY_PRESSED for steering
        keys = pygame.key.get_pressed()

        for key in keys:
            if keys[pygame.K_LEFT]:
                self.dir = -1, 0
                return
            if keys[pygame.K_RIGHT]:
                self.dir = 1, 0
                return
            if keys[pygame.K_UP]:
                self.dir = 0, -1
                return
            if keys[pygame.K_DOWN]:
                self.dir = 0, 1
                return

        newPos = self.pos[0] + self.dir[0] * self.dimensions[0], self.pos[1] + self.dir[1] * self.dimensions[1]

        if (board.canMove(newPos)): self.pos = newPos
        else: print('cant move!')

    