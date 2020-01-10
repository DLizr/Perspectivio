import math

import numpy as np


class Rotation:

    def __init__(self, width: float, vertices: list, centerPosition: list, startingDegrees=None):
        self.__centerPos = centerPosition
        self.__width = width
        if startingDegrees:
            self.__degrees = startingDegrees
        else:
            self.__degrees = [0] * (len(vertices) // 3)

    def update(self, vertices) -> np.ndarray:

        for i in range(0, len(vertices), 3):
            deg = self.__degrees[i // 3]
            x, z = 0, 0

            if deg != -1:
                x = self.__width * math.cos(math.radians(deg))
                z = self.__width * math.sin(math.radians(deg))
                self.__degrees[i // 3] += 3
            
            if deg == 360:
                self.__degrees[i // 3] = 0

            vertices[i] = self.__centerPos[0] - x
            vertices[i + 2] = self.__centerPos[2] - z

