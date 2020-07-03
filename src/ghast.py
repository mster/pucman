from src.board.history import History

# import core modules and community packages
import pygame
import random, time

class Ghast():
    def __init__(self, start, color=None, name=None):
        # get a good seed
        random.seed(int(time.time() + random.random()))

        # bind params
        self.pos = start
        self.name = name

        # props
        self.dimensions = 20,20
        self.color = color or (int(random.random() * 255), int(random.random() * 255), int(random.random() * 255))
        self.stepSize = 20, 20

        # for current hunting algo
        self.history = History(30)
        

    def draw(self, surface):
        x = self.pos[0]
        y = self.pos[1]

        w = self.dimensions[0]
        h = self.dimensions[1]

        # ghast body
        pygame.draw.circle(surface, self.color, (x + 10, y + 10), 10)

        # ghast eyes
        pygame.draw.circle(surface, (255,255,255), (x + 4, y + 7), 5)
        pygame.draw.circle(surface, (255,255,255), (x + 14, y + 7), 5)

    def move(self, pos, board):
        # directionals
        def LEFT(): 
            return (self.pos[0] - self.stepSize[0], self.pos[1])
        def RIGHT():
            return (self.pos[0] + self.stepSize[0], self.pos[1])
        def UP():
            return (self.pos[0], self.pos[1] - self.stepSize[1])
        def DOWN():
            return (self.pos[0], self.pos[1] + self.stepSize[1])

        # use pathfinder to move toward Pucman
        def HUNT():
            moveMap = [
                board.canMove(LEFT()) and LEFT() not in self.history._,
                board.canMove(RIGHT()) and RIGHT() not in self.history._,
                board.canMove(UP()) and UP() not in self.history._,
                board.canMove(DOWN()) and DOWN() not in self.history._
            ]

            horizontalPriority = abs(self.pos[0] - pos[0]) > abs(self.pos[1] - pos[1])
            favorLeft = self.pos[0] > pos[0]
            favorUp = self.pos[1] > pos[1]

            if (random.random() > 0.5):
                if moveMap[0] and favorLeft: 
                    self.pos = LEFT()
                elif moveMap[1]: 
                    self.pos = RIGHT()
                else:
                    if moveMap[2] and favorUp: 
                        self.pos = UP()
                    elif moveMap[3]: 
                        self.pos = DOWN()
            else:
                if moveMap[2] and favorUp: 
                    self.pos = UP()
                elif moveMap[3]: 
                    self.pos = DOWN()
                else:
                    if moveMap[0] and favorLeft: self.pos = LEFT()
                    elif moveMap[1]: self.pos = RIGHT()

        # wander randomly
        def WANDER():
            moveMap = [
                board.canMove(LEFT()),
                board.canMove(RIGHT()),
                board.canMove(UP()),
                board.canMove(DOWN())
            ]

            roll = int(random.random() * 4)

            if (roll == 0 and moveMap[0]):
                self.pos = LEFT()
            elif (roll == 1  and moveMap[1]):
                self.pos = RIGHT()
            elif (roll == 2  and moveMap[2]):
                self.pos = UP()
            elif (roll == 3 and moveMap[3]):
                self.pos = DOWN()
            else:
                WANDER()

        # coinflip hunt vs wander
        WANDER() if random.random() > 0.5 else HUNT()

        # enqueue position to history
        self.history.eq(self.pos)

        
    def atPucman(self, pos):
        if self.pos == pos: 
            return True
        else: 
            return False
        