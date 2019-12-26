from OpenGL.GL import GL_TRIANGLES

from src.rendering.object.StaticSceneObject import StaticSceneObject
from src.rendering.object.Wireframe import Wireframe


class StaticPyramid(StaticSceneObject):

    def __init__(self, centerPosition: list, sideWidth, colors: list=None):
        self.__side = sideWidth
        vertices = self.__genVertices(centerPosition)
        indices = [
            0, 1, 2,
            0, 1, 3,
            0, 2, 4,
            0, 3, 4,
            1, 2, 3,
            4, 2, 3
        ]
        if not colors:
            colors = [1.0] * 15
        super().__init__(vertices, indices, colors)
        self._centerPosition = centerPosition
        self.__genWireframe(vertices)
    
    def __genVertices(self, pos) -> list:
        halfSide = self.__side / 2
        vertices = [
            pos[0], pos[1] + self.__side, pos[2],  # Top.
            pos[0] + halfSide, pos[1], pos[2] + halfSide,  # -
            pos[0] + halfSide, pos[1], pos[2] - halfSide,  # - The Bottom Square.
            pos[0] - halfSide, pos[1], pos[2] + halfSide,  # -
            pos[0] - halfSide, pos[1], pos[2] - halfSide,  # -
        ]
        return vertices
    
    def __genWireframe(self, vertices):
        indices = [
            0, 1, 0, 2, 0, 3, 0, 4,
            1, 2, 1, 3, 2, 4, 3, 4
        ]
        self.addChildObject(Wireframe(vertices, indices, [0, 0, 0]))

    # Override
    def getPosition(self):
        return self._centerPosition.copy()

    # Override
    def render(self):
        super().render(GL_TRIANGLES)
