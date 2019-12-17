import numpy as np

from src.rendering.object.StaticSceneObject import StaticSceneObject


class DynamicSceneObject(StaticSceneObject):

    def __init__(self, vertices: list, indices: list, colors: list=None):

        super().__init__(vertices, indices, colors)
        self.__vertices = np.array(vertices, dtype="float32")
        self._centerPosition: np.ndarray = None
    
    def __updateVertices(self):
        self.vertexBuffer.updateData(self.__vertices)
        self.__moveWireframe()
        
    def moveX(self, x: float):
        self.__vertices[0:-1:3] += x
        self._centerPosition[0] += x
        self.__updateVertices()
    
    def moveY(self, y: float):
        self.__vertices[1:-1:3] += y
        self._centerPosition[1] += y
        self.__updateVertices()
    
    def moveZ(self, z: float):
        self.__vertices[2:self.__vertices.size:3] += z
        self._centerPosition[2] += z
        self.__updateVertices()
    
    def getPosition(self) -> np.ndarray:
        """Returns a position.
        Must be overriden by the actual object class.
        ------------------"""
        raise NotImplementedError("Create a subtype dynamic object!")
    
    def __moveWireframe(self):
        for i in self._childObjects:
            i.updateVertices(self.__vertices)
    
    def __repr__(self):
        return "DynamicObject({})".format(type(self))
