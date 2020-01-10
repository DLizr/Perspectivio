import numpy as np


class Hovering:

    def __init__(self, vertices: list, dY: float):
        self.__vertices = vertices
        self.__dY = dY
        self.__currentDY = 0
        self.__direction = 1
    
    def update(self, vertices: np.ndarray):

        self.__currentDY += 0.008 * self.__direction
        if abs(self.__currentDY) >= self.__dY:
            self.__direction *= -1
        
        vertices += 0.008 * self.__direction
