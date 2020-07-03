# import board elements
from src.board.wall import Wall
from src.board.food import Food
from src.board.superFood import SuperFood
from src.config import *

# import core modules and community packages
import random
import pygame

class Board():
    def __init__(self, size, tileSize=(20,20), color=(0,0,0)):
        # init a new display called '_' with given dimensions
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

        # score and fitness
        self.score = 0

        # init board
        self.mapify()

    def draw(self):
        self._.fill(self.color)

        for x in range(self.xTileCount):
            for y in range(self.yTileCount):
                curr = self.tileMap[x][y]

                # add food
                if (curr == BOARD_ELEMENT_MAP['FOOD']):
                    coords = int(x * self.tileSize[0] + self.tileSize[0] / 2), int(y * self.tileSize[1] + self.tileSize[1] / 2)
                    # pygame.draw.circle(self._, (222, 161, 133), coords, 3)
                    Food(coords).draw(self._)
                
                # add wall
                elif (curr == BOARD_ELEMENT_MAP['WALL']):
                    coords = int(x * self.tileSize[0]), int(y * self.tileSize[1])
                    Wall(coords).draw(self._)

                # add super food
                elif (curr == BOARD_ELEMENT_MAP['SUPERFOOD']):
                    coords = int(x * self.tileSize[0] + self.tileSize[0] / 2), int(y * self.tileSize[1] + self.tileSize[1] / 2)
                    SuperFood(coords).draw(self._)

    

    def mapify(self):
        self.xTileCount = self.size[0] // self.tileSize[0]
        self.yTileCount = self.size[1] // self.tileSize[1]

        if (self.size[0] % self.tileSize[0] != 0):
            self.xOffset = self.size[0] % self.tileSize[0]
        if (self.size[1] % self.tileSize[1] != 0):
            self.yOffset = self.size[1] % self.tileSize[1]
        
        # init tileMap with all 1
        self.tileMap = [([1 for y in range(self.yTileCount)]) for x in range(self.xTileCount)]

        # add boarders to tileMap
        for x in range(self.xTileCount): 
            self.tileMap[x][0] = BOARD_ELEMENT_MAP['WALL']
            self.tileMap[x][self.yTileCount-1] = BOARD_ELEMENT_MAP['WALL']
        for y in range(self.yTileCount): 
            self.tileMap[0][y] = BOARD_ELEMENT_MAP['WALL']
            self.tileMap[self.xOffset-1][y] = BOARD_ELEMENT_MAP['WALL']

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

        self.tileMap[5][5] = 3

    def canMove(self, pos):
        x, y = self.getTile(pos)

        if (self.tileMap[x][y] == 2): return False
        else: return True

    def pucmanEat(self, pos):
        x, y = self.getTile(pos)

        # check if pucman actually ate the food
        score = 0
        curr = self.tileMap[x][y]
        if (curr == BOARD_ELEMENT_MAP['FOOD']): 
            score = 10
        if (curr == BOARD_ELEMENT_MAP['SUPERFOOD']):
            score = 50

        # this removes the food from the board
        self.tileMap[x][y] = 0

        return score


    def getTile(self, pos):
        x = pos[0] // self.tileSize[0]
        y = pos[1] // self.tileSize[1]

        return x, y
    