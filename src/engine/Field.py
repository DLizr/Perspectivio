import numpy as np


class Field:

    def __init__(self, width: int, height: int, depth: int):
        self.__field = np.array([[[None for _ in range(depth)] for _ in range(height)] for _ in range(width)])
        self.__width = width
        self.__height = height
        self.__depth = depth
    
    def placeObject(self, x: int, y: int, z: int, obj):
        self.__field[x][y][z] = obj
    
    def removeObject(self, x: int, y: int, z: int):
        self.__field[x][y][z] = None
    
    def canObjectMoveTo(self, obj, x: int, y: int, z: int) -> bool:
        if x<0 or y<0 or z<0:
            return False
        try:
            return self.__field[x][y][z] == obj or not self.__field[x][y][z]  # An object can stay in its own position and move to an empty cell.
        except IndexError:
            return False
    
    def __getTilesNearby(self, x: int, y: int, z: int):
        x1 = max(0, x-1)
        y1 = max(0, y-1)
        z1 = max(0, z-1)
        x2 = min(x+2, self.__width)
        y2 = min(y+2, self.__height)
        z2 = min(z+2, self.__depth)

        return self.__field[x1:x2, y1:y2, z1:z2].flatten()
    
    def moveObject(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int):
        try:
            obj = self.__field[x1][y1][z1]
            self.__field[x1][y1][z1] = None
            self.__field[x2][y2][z2] = obj
        except IndexError:
            raise IndexError("Moving out of the field")
