from src.config import SCORE_VALUES, POWER_UP_LENGTH, TICK_RATE

# import core modules and community packages
import pygame

class Pucman():
    def __init__(self, start, color=(255,255,0), MODE="PLAYING"):
        # bind params
        self.pos = start
        self.MODE = MODE

        # props
        self.dimensions = 20,20
        self.color = color
        self.dir = 0,0
        self.score = 0
        self.isPoweredUp = False
        self.ticker = 0


    def draw(self, surface):
        x = self.pos[0] + self.dimensions[0]//2
        y = self.pos[1] + self.dimensions[1]//2

        w = self.dimensions[0]
        h = self.dimensions[1]
        radius = min(w//2,h//2)

        # draw body
        if (self.isPoweredUp):
            pygame.draw.circle(surface, (255,0,0), (x, y), radius)
        else:
            pygame.draw.circle(surface, self.color, (x, y), radius)

        # mouth left
        if (self.dir == (-1, 0)): 
            pygame.draw.polygon(surface, (0,0,0), [
                (self.pos[0], self.pos[1]),
                (self.pos[0], self.pos[1] + self.dimensions[1]),
                (x,y)
            ])

        # mouth down
        elif (self.dir == (0, 1)):
            pygame.draw.polygon(surface, (0,0,0), [
                (self.pos[0], self.pos[1] + self.dimensions[1]),
                (self.pos[0] + self.dimensions[0], self.pos[1] + self.dimensions[1]),
                (x,y)
            ])

        # mouth up
        elif (self.dir == (0, -1)):
            pygame.draw.polygon(surface, (0,0,0), [
                (self.pos[0], self.pos[1]),
                (self.pos[0] + self.dimensions[0], self.pos[1]),
                (x,y)
            ])

        # mouth right as default
        else: 
            pygame.draw.polygon(surface, (0,0,0), [
                (self.pos[0] + self.dimensions[0], self.pos[1]),
                (self.pos[0] + self.dimensions[0], self.pos[1] + self.dimensions[1]),
                (x,y)
            ])

        print(self.score)

        
    def move(self, board):
        self.ticker -= 1

        # check for QUIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # check KEY_PRESSED for steering
        keys = pygame.key.get_pressed()

        for key in keys:
            if keys[pygame.K_LEFT]:
                self.dir = -1, 0
                #return
            if keys[pygame.K_RIGHT]:
                self.dir = 1, 0
                #return
            if keys[pygame.K_UP]:
                self.dir = 0, -1
                #return
            if keys[pygame.K_DOWN]:
                self.dir = 0, 1
                #return

        newPos = self.pos[0] + self.dir[0] * self.dimensions[0], self.pos[1] + self.dir[1] * self.dimensions[1]

        if (board.canMove(newPos)): 
            self.pos = newPos

            actionValue = board.pucmanEat(self.pos)
            if (actionValue == SCORE_VALUES['SUPERFOOD']):
                self.isPoweredUp = True
                self.ticker = TICK_RATE[self.MODE] * POWER_UP_LENGTH

            self.score = self.score + actionValue
        else: 
            print('cant move!')

        if (self.ticker == 0):
            self.isPoweredUp = False

class Ticker():
    def __init__(self, until):
        self.tick = until

    