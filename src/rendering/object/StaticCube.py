import numpy as np

from src.rendering.object.StaticSceneObject import StaticSceneObject
from src.rendering.object.Wireframe import Wireframe


class StaticCube(StaticSceneObject):

    def __init__(self, centerPosition: list, width, colors: list=None):
        self.__width = width
        vertices = self.genVertices(centerPosition)
        indices = [1, 3, 7, 5, 
                   3, 2, 6, 7, 
                   2, 6, 4, 0, 
                   0, 4, 5, 1, 
                   1, 3, 2, 0, 
                   7, 6, 4, 5]
        if not colors:
            colors = [1.0] * 24
        super().__init__(vertices, indices, colors)
        self._centerPosition = centerPosition
        self.__genWireframe(vertices)
    
    def genVertices(self, centerPos) -> list:
        vertices = []
        offset = [-self.__width / 2, self.__width / 2]
        for x in offset:
            for y in offset:
                for z in offset:
                    vertices.extend([float(centerPos[0] + x), 
                                     float(centerPos[1] + y), 
                                     float(centerPos[2] + z)])
        return vertices
    
    def __genWireframe(self, vertices):
        indices = [0, 1, 1, 3, 3, 2, 2, 0,
                   2, 6, 6, 4, 4, 0,
                   6, 7, 7, 5, 5, 4,
                   7, 3, 1, 5]
        color = [0, 0, 0]
        self.addChildObject(Wireframe(vertices, indices, color))
    
    def getPosition(self) -> list:
        return self._centerPosition.copy()
    
    def getWidth(self) -> int:
        return self.__width
    
    @staticmethod
    def getShape() -> str:
        return "Cube"
