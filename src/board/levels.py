# 
from src.config import BOARD_ELEMENT_MAP

N = BOARD_ELEMENT_MAP['NONE']
W = BOARD_ELEMENT_MAP['WALL']
F = BOARD_ELEMENT_MAP['FOOD']
S = BOARD_ELEMENT_MAP['SUPERFOOD']
P = BOARD_ELEMENT_MAP['PUCMAN_START']
G = BOARD_ELEMENT_MAP['GHAST_SPAWN']

LEVEL_1 = [
    [W, W, W, W, W, F, W, W, W, W, W],
    [W, P, F, F, F, F, F, F, F, F, W],
    [W, F, W, W, W, F, W, W, W, F, W],
    [W, F, W, S, F, F, F, S, W, F, W],
    [W, F, F, F, F, F, F, F, F, F, W],
    [F, F, F, F, F, G, F, F, F, F, F],
    [W, F, F, F, F, F, F, F, F, F, W],
    [W, F, W, S, F, F, F, S, W, F, W],
    [W, F, W, W, W, F, W, W, W, F, W],
    [W, F, F, F, F, F, F, F, F, F, W],
    [W, W, W, W, W, F, W, W, W, W, W],
]
