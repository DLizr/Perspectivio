from OpenGL.GL import GL_TRIANGLES

from src.rendering.object.StaticSceneObject import StaticSceneObject
from src.rendering.object.Wireframe import Wireframe


class Powerup(StaticSceneObject):

    def __init__(self, centerPosition: list, width, colors: list=None):
        self.__width = width
        self.__action = None
        vertices = self.__genVertices(centerPosition)

        indices = [
            0, 1, 2,
            0, 1, 4,
            0, 3, 4,
            0, 2, 3,

            1, 2, 5,
            2, 5, 6,

            2, 3, 6,
            3, 6, 7,

            3, 4, 7,
            4, 7, 8,

            1, 4, 5,
            4, 5, 8,

            5, 6, 9,
            6, 7, 9,
            7, 8, 9,
            5, 8, 9
        ]

        if not colors:
            colors = [0.0, 1.0, 0.0] * 10
        
        super().__init__(vertices, indices, colors)
        self._centerPosition = centerPosition
        self.__genWireframe(vertices)
    
    def __genVertices(self, pos):
        halfWidth = self.__width / 2
        quaterWidth = self.__width / 4
        vertices = [
            pos[0], pos[1] + halfWidth, pos[2],  # Top

            pos[0] - quaterWidth, pos[1] + quaterWidth, pos[2],  #
            pos[0], pos[1] + quaterWidth, pos[2] - quaterWidth,  # Upper
            pos[0] + quaterWidth, pos[1] + quaterWidth, pos[2],  # Triangles
            pos[0], pos[1] + quaterWidth, pos[2] + quaterWidth,  #

            pos[0] - quaterWidth, pos[1] - quaterWidth, pos[2],  #
            pos[0], pos[1] - quaterWidth, pos[2] - quaterWidth,  # Lower
            pos[0] + quaterWidth, pos[1] - quaterWidth, pos[2],  # Triangles
            pos[0], pos[1] - quaterWidth, pos[2] + quaterWidth,  #

            pos[0], pos[1] - halfWidth, pos[2]  # Bottom
        ]

        return vertices
    
    def __genWireframe(self, vertices):
        indices = [
            0, 1, 0, 2, 0, 3, 0, 4,
            1, 2, 2, 3, 3, 4, 1, 4,
            1, 5, 2, 6, 3, 7, 4, 8,
            5, 6, 6, 7, 7, 8, 5, 8,
            5, 9, 6, 9, 7, 9, 8, 9
        ]
        self.addChildObject(Wireframe(vertices, indices, [0, 0, 0]))
    
    def setAction(self, action):
        self.__action = action
    
    def onImpact(self, game):
        if self.__action:
            self.__action.onImpact(game)
    
    # Override
    def getPosition(self):
        return self._centerPosition.copy()

    def getWidth(self):
        return self.__width / 2
    
    def getHeight(self):
        return self.__width

    # Override
    def render(self):
        super().render(GL_TRIANGLES)
    
    @staticmethod
    def getShape():
        return "Rectangle"
        
