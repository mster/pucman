# pac-ai

# import core modules and community packages
import sys, math, random
import pygame

# import configuration settings
from src.config import *

# import game elements
from src.pucman import Pucman
from src.ghast import Ghast
from src.board.board import Board


def main ():
    # initialize all imported pygame modules
    pygame.init()

    # initialize game elements
    board = Board(size=BOARD_SIZE)
    pucman = Pucman(start=START['PUCMAN'], color=COLOR['PUCMAN'])
    ghasts = {
        "blinky": Ghast(start=START['GHAST'], color=COLOR['BLINKY'], name="Blinky"),
        "pinky": Ghast(start=START['GHAST'], color=COLOR['PINKY'], name="Pinky"),
        "inky": Ghast(start=START['GHAST'], color=COLOR['INKY'], name="Inky"),
        "clyde": Ghast(start=START['GHAST'], color=COLOR['CLYDE'], name="Clyde")
    }

    # configure game clock
    clock = pygame.time.Clock()

    # draw background & begin session
    board.draw()
    session = True

    # while playing
    while session:
        # manage game time, 5 ticks per second
        clock.tick(TICK_RATE['PLAYING'])
        pygame.time.delay(50)

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

    # DEV: auto-restart game after a loss
    main()

if __name__ == "__main__":
    main()

