from src.config import SCORE_VALUES, POWER_UP_LENGTH, TICK_RATE

# import core modules and community packages
import pygame

class Pucman():
    def __init__(self, start, size, color=(255,255,0), MODE="PLAYING"):
        # bind params
        self.start = start
        self.pos = start
        self.mode = MODE

        # props
        self.dimensions = size
        self.color = color
        self.dir = 0,0
        self.score = 0
        self.isPoweredUp = False
        self.ticker = 0


    def draw(self, surface):
        x = self.pos[0]
        y = self.pos[1]

        c_x = self.pos[0] + self.dimensions[0]//2
        c_y = self.pos[1] + self.dimensions[1]//2

        w = self.dimensions[0]
        h = self.dimensions[1]

        radius = min(w//2,h//2)

        # draw body
        if (self.isPoweredUp):
            pygame.draw.circle(surface, (255,0,0), (c_x, c_y), radius)
        else:
            pygame.draw.circle(surface, self.color, (c_x, c_y), radius)

        # mouth left
        if (self.dir == (-1, 0)): 
            pygame.draw.polygon(surface, (0,0,0), [
                (x, y),
                (x, y + h),
                (c_x, c_y)
            ])

        # mouth down
        elif (self.dir == (0, 1)):
            pygame.draw.polygon(surface, (0,0,0), [
                (x, y + h),
                (x + w, y + h),
                (c_x, c_y)
            ])

        # mouth up
        elif (self.dir == (0, -1)):
            pygame.draw.polygon(surface, (0,0,0), [
                (x, y),
                (x + w, y),
                (c_x,c_y)
            ])

        # mouth right as default
        else: 
            pygame.draw.polygon(surface, (0,0,0), [
                (x + w, y),
                (x + w, y + h),
                (c_x, c_y)
            ])

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
            if keys[pygame.K_RIGHT]:
                self.dir = 1, 0
            if keys[pygame.K_UP]:
                self.dir = 0, -1
            if keys[pygame.K_DOWN]:
                self.dir = 0, 1

        x = self.pos[0]
        y = self.pos[1]
        deltaX = self.dir[0] * self.dimensions[0]
        deltaY = self.dir[1] * self.dimensions[1]
        newPos = (x + deltaX, y + deltaY)

        canMove = board.canMove(newPos)
        canJump = board.canJump(newPos)

        # move if possible
        if (canMove or canJump):
            if (not canMove):
                self.pos = canJump
            else: 
                self.pos = newPos

            # interpret result of the move
            actionValue = board.pucmanEat(self.pos)
            if (actionValue == SCORE_VALUES['SUPERFOOD']):
                self.isPoweredUp = True
                self.ticker = TICK_RATE[self.mode] * POWER_UP_LENGTH

            # update current score
            self.score = self.score + actionValue
        elif (self.mode == 'DEV'): 
            print('cant move!')

        # update power up
        if (self.ticker == 0):
            self.isPoweredUp = False
        
        if (self.mode == 'DEV'):
            print(self.score)

    def reset (self):
        pass
