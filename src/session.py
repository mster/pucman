# import core modules and community packages
import sys, math, random
import pygame

# import configuration settings
from src.config import *
from src.board.levels import LEVEL_1

# import game elements
from src.pucman import Pucman
from src.ghast import Ghast
from src.board.board import Board

class Session():
    def __init__(self, MODE="PLAYING"):
        # init all game props
        pygame.init()

        # initialize game elements
        board = Board(
            size=BOARD_SIZE, 
            color=COLOR['BACKGROUND'], 
            level=LEVEL_1
        )
        pucman = Pucman(
            start=board.findUniquePos(BOARD_ELEMENT_MAP['PUCMAN_START']), 
            size=board.tileSize, 
            color=COLOR['PUCMAN'], 
            MODE=MODE
        )
        ghasts = {
            "blinky": Ghast(
                name="Blinky",
                start=board.findUniquePos(BOARD_ELEMENT_MAP['GHAST_SPAWN']), 
                size=board.tileSize, 
                color=COLOR['BLINKY']
            ),
            "pinky": Ghast(
                name="Pinky",
                start=board.findUniquePos(BOARD_ELEMENT_MAP['GHAST_SPAWN']), 
                size=board.tileSize, 
                color=COLOR['PINKY']
            ),
            "inky": Ghast(
                name="Inky",
                start=board.findUniquePos(BOARD_ELEMENT_MAP['GHAST_SPAWN']), 
                size=board.tileSize, 
                color=COLOR['INKY']
            ),
            "clyde": Ghast(
                name="Clyde",
                start=board.findUniquePos(BOARD_ELEMENT_MAP['GHAST_SPAWN']), 
                size=board.tileSize, 
                color=COLOR['CLYDE'] 
            )
        }

        self.board = board
        self.pucman = pucman
        self.ghasts = ghasts
        self.clock = pygame.time.Clock()
        self.MODE = MODE

    def start(self):
        # draw background & begin session
        self.board.draw()
        session = True

        # while playing
        while session:
            # manage game time, 5 ticks per second
            self.clock.tick(TICK_RATE[self.MODE])
            # pygame.time.delay(50)

            # update player state
            self.pucman.move(self.board)

            # Ghast-AI behavior
            for ghast in self.ghasts:
                sprite = self.ghasts[ghast]

                sprite.move(self.pucman.pos, self.board)
                if(sprite.atPucman(self.pucman.pos)):
                    session = False
                    print("You died to " + sprite.name)

            # begin drawing back to front
            self.board.draw()
            self.pucman.draw(self.board._)
            for ghast in self.ghasts:
                self.ghasts[ghast].draw(self.board._)
                
            # update board
            pygame.display.update()
