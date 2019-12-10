import numpy as np


class Field:

    def __init__(self, width: int, height: int, depth: int):
        self.__field = [[[None for _ in range(depth)] for _ in range(height)] for _ in range(width)]
    
    def placeObject(self, x: int, y: int, z: int, obj):
        self.__field[x][y][z] = obj
    
    def removeObject(self, x: int, y: int, z: int):
        self.__field[x][y][z] = None
    
    # TODO: Collision, movement, borders.
