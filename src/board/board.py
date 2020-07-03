from src.board.wall import Wall

import random
import pygame

class Board():
    def __init__(self, size, tileSize=(20,20), color=(0,0,0)):
        # print('Board.__init__()')
        self._ = pygame.display.set_mode(size)
        self._.fill(color)

        # bind
        self.size = size
        self.color = color
        self.tileSize = tileSize

        # board state
        self.tileMap = None
        self.xOffset = 0
        self.yOffset = 0
        self.xTileCount = 0
        self.yTileCount = 0

        self.score = 0

        self.gridify()

    def draw(self):
        self._.fill(self.color)

        for x in range(self.xTileCount):
            for y in range(self.yTileCount):
                # food vs wall
                if (self.tileMap[x][y] == 1):
                    coords = int(x * self.tileSize[0] + self.tileSize[0] / 2), int(y * self.tileSize[1] + self.tileSize[1] / 2)
                    pygame.draw.circle(self._, (222, 161, 133), coords, 3)
                elif (self.tileMap[x][y] == 2):
                    coords = int(x * self.tileSize[0]), int(y * self.tileSize[1])
                    Wall(coords).draw(self._)

    def generate(self):
        pass
    

    def gridify(self):
        self.xTileCount = self.size[0] // self.tileSize[0]
        self.yTileCount = self.size[1] // self.tileSize[1]
        print(self.xTileCount, self.yTileCount)

        if (self.size[0] % self.tileSize[0] != 0):
            self.xOffset = self.size[0] % self.tileSize[0]
        if (self.size[1] % self.tileSize[1] != 0):
            self.yOffset = self.size[1] % self.tileSize[1]
        
        # init tileMap with all 1
        self.tileMap = [([1 for y in range(self.yTileCount)]) for x in range(self.xTileCount)]

        # add boarders to tileMap
        for x in range(self.xTileCount): 
            self.tileMap[x][0] = 2
            self.tileMap[x][self.yTileCount-1] = 2
        for y in range(self.yTileCount): 
            self.tileMap[0][y] = 2
            self.tileMap[self.xOffset-1][y] = 2

        # this is temporary
        # adds a starting zone for ghosts
        self.tileMap[12][10] = 2
        self.tileMap[12][11] = 2
        self.tileMap[12][12] = 2
        self.tileMap[12][9] = 2
        self.tileMap[12][8] = 2
        self.tileMap[12][13] = 2
        self.tileMap[12][14] = 2
        self.tileMap[12][15] = 2
        self.tileMap[12][16] = 2

        self.tileMap[18][10] = 2
        self.tileMap[18][11] = 2
        self.tileMap[18][12] = 2
        self.tileMap[18][9] = 2
        self.tileMap[18][8] = 2
        self.tileMap[18][13] = 2
        self.tileMap[18][14] = 2
        self.tileMap[18][15] = 2
        self.tileMap[18][16] = 2

        self.tileMap[13][8] = 2
        self.tileMap[14][8] = 2
        self.tileMap[15][8] = 2
        self.tileMap[16][8] = 2
        self.tileMap[17][8] = 2

    def canMove(self, pos):
        x = pos[0] // self.tileSize[0]
        y = pos[1] // self.tileSize[1]

        if (self.tileMap[x][y] == 2):
            return False
        else:
            return True

    def pucmanEat(self):
        pass
    