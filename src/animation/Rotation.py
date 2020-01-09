import math

import numpy as np


class Rotation:

    def __init__(self, vertices: list, centerPosition: list, startingDegrees=None):
        self.__vertices = vertices
        self.__centerPos = centerPosition
        if startingDegrees:
            self.__degrees = startingDegrees
        else:
            self.__degrees = [0] * (len(vertices) // 3)

    def update(self) -> list:
        newVertices = []

        for i in range(0, len(self.__vertices), 3):
            deg = self.__degrees[i // 3]
            v1, v2, v3 = self.__vertices[i:i+3]
            x, z = 0, 0

            if deg != -1:
                x = 0.5 * math.cos(math.radians(deg))
                z = 0.5 * math.sin(math.radians(deg))
                self.__degrees[i // 3] += 3

            newVertices.append(self.__centerPos[0] - x)
            newVertices.append(v2)
            newVertices.append(self.__centerPos[2] - z)

        return newVertices
