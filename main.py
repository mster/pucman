# pac-ai

# import core modules
import sys, math, random

# import game session
from src.session import Session

MODE = 'PLAYING'

def main ():
    sesh = Session()
    sesh.start()

if __name__ == "__main__":
    main()

