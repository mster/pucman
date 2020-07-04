# pac-ai

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

MODE = 'PLAYING'

def main ():
    print('main')
    # initialize all imported pygame modules
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

    # configure game clock
    clock = pygame.time.Clock()

    # draw background & begin session
    board.draw()
    session = True

    # while playing
    while session:
        # manage game time, 5 ticks per second
        clock.tick(TICK_RATE[MODE])
        # pygame.time.delay(50)

        # update player state
        pucman.move(board)

        # begin drawing back to front
        board.draw()
        pucman.draw(board._)

        # AI ghasts
        for ghast in ghasts:
            sprite = ghasts[ghast]

            sprite.move(pucman.pos, board)
            session = not sprite.atPucman(pucman.pos)
            if not session:
                # losing condition: 1 or more ghasts touched Pucman
                print("You died to " + sprite.name)
                break

            # end AI behavior by drawing ghast
            sprite.draw(board._)

        # update board
        pygame.display.update()

if __name__ == "__main__":
    main()

