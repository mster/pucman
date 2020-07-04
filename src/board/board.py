# import board elements
from src.board.wall import Wall
from src.board.food import Food
from src.board.superFood import SuperFood
from src.config import *

# import core modules and community packages
import random
import pygame

class Board():
    def __init__(self, size, level=None, color=(0,0,0)):
        # init a new display called '_' with given dimensions
        self._ = pygame.display.set_mode(size)
        self._.fill(color)

        # bind
        self.size = size
        self.color = color
        self.tileMap = level

        # board state
        self.tileSize = None
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
                    Food(coords, self.tileSize).draw(self._)
                
                # add wall
                elif (curr == BOARD_ELEMENT_MAP['WALL']):
                    coords = int(x * self.tileSize[0]), int(y * self.tileSize[1])
                    Wall(coords, self.tileSize).draw(self._)

                # add super food
                elif (curr == BOARD_ELEMENT_MAP['SUPERFOOD']):
                    coords = int(x * self.tileSize[0] + self.tileSize[0] / 2), int(y * self.tileSize[1] + self.tileSize[1] / 2)
                    SuperFood(coords, self.tileSize).draw(self._)

    def mapify(self):
        self.tileSize = self.size[0] // len(self.tileMap), self.size[1] // len(self.tileMap[0])
        self.xTileCount = self.size[0] // self.tileSize[0]
        self.yTileCount = self.size[1] // self.tileSize[1]

    def findUniquePos(self, key):
        x = y = None
        for i in range(len(self.tileMap)):      
            for j in range(len(self.tileMap[0])):
                if self.tileMap[i][j] == key:
                    x = i * self.tileSize[0]
                    y = j * self.tileSize[1]
        return (x, y)

    def canMove(self, pos):
        x, y = self.getTile(pos)

        # check for out of index
        if (x < 0 or x >= self.xTileCount or y < 0 or y >= self.yTileCount):
            return False

        # normal behavior
        curr = self.tileMap[x][y]
        if (curr == BOARD_ELEMENT_MAP['WALL']):
            return False
        else: 
            return True

        print('move', pos)

    def canJump(self, pos):
        # check if our move counts as a jump
        x, y = self.getTile(pos)
        landingTile = (x, y)

        # x-jump OVER
        if (x >= self.xTileCount):
            landingTile = 0, landingTile[1]

        # y-jump OVER
        elif (y >= self.yTileCount):
            landingTile = landingTile[0], 0
        
        # x-jump UNDER
        elif (x < 0):
            landingTile = self.xTileCount - 1, landingTile[1]

        # y-jump UNDER
        elif (y < 0):
            landingTile = landingTile[0], self.yTileCount - 1

        landingPos = self.getPos(landingTile)
        landingValue = self.tileMap[landingTile[0]][landingTile[1]]

        # pucman can't jump over walls
        if (landingValue == BOARD_ELEMENT_MAP['WALL']):
            return False
        else:
            return landingPos

    def pucmanEat(self, pos):
        x, y = self.getTile(pos)
        curr = self.tileMap[x][y]

        # check if pucman ate food
        score = 0
        if (curr == BOARD_ELEMENT_MAP['FOOD']): 
            score = 10
        if (curr == BOARD_ELEMENT_MAP['SUPERFOOD']):
            score = 50

        self.tileMap[x][y] = BOARD_ELEMENT_MAP['NONE']
        return score

    def getTile(self, pos):
        # get tile from position
        x = pos[0] // self.tileSize[0]
        y = pos[1] // self.tileSize[1]

        return x, y

    def getPos(self, tile):
        # get position from tile
        x = tile[0] * self.tileSize[0]
        y = tile[1] * self.tileSize[1]

        return x, y
    