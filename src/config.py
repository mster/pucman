BOARD_SIZE = 620, 620 # pixels

START = {
    'PUCMAN': (20, 20),
    'GHAST': (300, 300)
}

COLOR = {
    'BACKGROUND': (0, 0, 0),
    'PUCMAN': (255, 255, 0),
    'BLINKY': (255, 0, 0),
    'PINKY': (255, 184, 255),
    'INKY': (0, 255, 255),
    'CLYDE': (255, 184, 82),
    'FOOD': (222, 161, 133)
}

BOARD_ELEMENT_MAP = {
    'NONE': 0,
    'FOOD': 1,
    'WALL': 2,
    'SUPERFOOD': 3
}

TICK_RATE = {
    'DEV': 1,
    'PLAYING': 5,
    'TRAINING': 50
}

SCORE_VALUES = {
    'FOOD': 10,
    'SUPERFOOD': 50
}

POWER_UP_LENGTH = 10 # seconds