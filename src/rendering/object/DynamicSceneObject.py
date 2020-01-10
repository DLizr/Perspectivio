import numpy as np

from src.rendering.object.StaticSceneObject import StaticSceneObject


class DynamicSceneObject(StaticSceneObject):

    def __init__(self, vertices: list, indices: list, colors: list=None):

        super().__init__(vertices, indices, colors)
        self._vertices = np.array(vertices, dtype="float32")
        self._centerPosition: np.ndarray = None
    
    def _updateVertices(self):
        self.vertexBuffer.updateData(np.array(self._vertices, dtype="float32"))
        self.__moveWireframe()
        
    def moveX(self, x: float):
        self._vertices[0:-1:3] += x
        self._centerPosition[0] += x
        self._updateVertices()
    
    def moveY(self, y: float):
        self._vertices[1:-1:3] += y
        self._centerPosition[1] += y
        self._updateVertices()
    
    def moveZ(self, z: float):
        self._vertices[2:len(self._vertices):3] += z
        self._centerPosition[2] += z
        self._updateVertices()
    
    def getPosition(self) -> np.ndarray:
        """Returns a position.
        Must be overriden by the actual object class.
        ------------------"""
        raise NotImplementedError("Create a subtype dynamic object!")

    def getWidth(self):
        raise NotImplementedError("Create a subtype dynamic object!")
    
    def __moveWireframe(self):
        for i in self._childObjects:
            i.updateVertices(self._vertices)

    def update(self):
        return
    
    def __repr__(self):
        return "DynamicObject({})".format(type(self))
