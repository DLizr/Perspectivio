import numpy as np

from src.lowlevel.VertexBufferObject import VBO
from src.lowlevel.IndexBufferObject import IBO
from src.rendering.object.StaticSceneObject import StaticSceneObject


class DynamicSceneObject(StaticSceneObject):

    def __init__(self, vertices: list, indices: list, colors: list=None):

        super().__init__(vertices, indices, colors)
        self.vertices = np.array(vertices, dtype="float32")
    
    def __updateVertices(self):
        self.vertexBuffer.updateData(self.vertices)
        
    def moveX(self, x: float):
        self.vertices[0:-1:3] += x
        self.__updateVertices()
    
    def moveY(self, y: float):
        self.vertices[1:-1:3] += y
        self.__updateVertices()
    
    def moveZ(self, z: float):
        self.vertices[2:self.vertices.size:3] += z
        self.__updateVertices()
