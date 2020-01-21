import numpy as np


class Field:

    def __init__(self, width: int, height: int, depth: int):
        self.__field = np.array([[[None for _ in range(depth)] for _ in range(height)] for _ in range(width)])
        self.__dynamicField = dict()
        self.__width = width
        self.__height = height
        self.__depth = depth
    
    def placeObject(self, obj, x: int, y: int, z: int):
        if x >= self.__width:
            self.__field = np.concatenate((self.__field, np.zeros((x + 1 - self.__width, self.__height, self.__depth))), axis=0)
        if y >= self.__height:
            self.__field = np.concatenate((self.__field, np.zeros((self.__width, y + 1 - self.__height, self.__depth))), axis=1)
        if z >= self.__depth:
            self.__field = np.concatenate((self.__field, np.zeros((self.__width, self.__height, z + 1 - self.__depth))), axis=2)
        self.__field[x][y][z] = obj
    
    def placeDynamicObject(self, obj, x: int, y: int, z: int):
        self.__dynamicField[obj] = (x, y, z)
    
    def removeObject(self, x: int, y: int, z: int):
        self.__field[x][y][z] = None
    
    def canMoveTo(self, x: int, y: int, z: int) -> bool:
        return (0 <= x < self.__width and 
                0 <= y < self.__height and 
                0 <= z < self.__depth)
    
    def getTilesNearby(self, x: int, y: int, z: int, ignoreX=False, ignoreY=False, ignoreZ=False):
        x1 = max(0, x-1) if not ignoreX else 0
        y1 = max(0, y-1) if not ignoreY else 0
        z1 = max(0, z-1) if not ignoreZ else 0
        x2 = min(x+2, self.__width) if not ignoreX else self.__width
        y2 = min(y+2, self.__height) if not ignoreY else self.__height
        z2 = min(z+2, self.__depth) if not ignoreZ else self.__depth

        return self.__field[x1:x2, y1:y2, z1:z2].flatten()
    
    def getTilesUnder(self, x: int, y: int, z: int, ignoreX=False, ignoreY=False, ignoreZ=False):
        x1 = max(0, x-1) if not ignoreX else 0
        z1 = max(0, z-1) if not ignoreZ else 0
        y1 = max(0, y-1) if not ignoreY else 0
        x2 = min(x+2, self.__width) if not ignoreX else self.__width
        y2 = y if not ignoreY else self.__height
        z2 = min(z+2, self.__depth) if not ignoreZ else self.__depth

        return self.__field[x1:x2, y1:y2, z1:z2].flatten()
    
    def moveObject(self, obj, x: int, y: int, z: int):
        self.__dynamicField[obj] = (x, y, z)
    
    def getSize(self) -> tuple:
        return (self.__width, self.__height, self.__depth)
