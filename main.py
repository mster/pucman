# pac-ai

import sys, math, random
import pygame

from src.pucman import Pucman
from src.ghast import Ghast
from src.board.board import Board

def main ():
    # init game and props
    pygame.init()

    board = Board(size=(620,620))
    pucman = Pucman(start=(20,20))
    ghasts = {
        "blinky": Ghast(start=(300,300), color=(255, 0, 0), name="Blinky"),
        "pinky": Ghast(start=(300,300), color=(255, 184, 255), name="Pinky"),
        "inky": Ghast(start=(300,300), color=(0, 255, 255), name="Inky"),
        "clyde": Ghast(start=(300,300), color=(255, 184, 82), name="Clyde")
    }

    clock = pygame.time.Clock()
    board.draw()

    session = True

    # while playing
    while session:
        # game time management
        pygame.time.delay(50)
        clock.tick(5)

        # updating game state
        pucman.move(board)

        board.draw()
        pucman.draw(board._)

        # AI ghosts
        for ghast in ghasts:
            sprite = ghasts[ghast]

            sprite.move(pucman.pos, board)
            session = not sprite.atPucman(pucman.pos)
            if not session:
                print("You died to " + sprite.name)
                break
            sprite.draw(board._)

        # update board
        pygame.display.update()

    main()

if __name__ == "__main__":
    main()

