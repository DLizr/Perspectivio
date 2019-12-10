import numpy as np

from src.lowlevel.VertexBufferObject import VBO
from src.lowlevel.IndexBufferObject import IBO


class StaticSceneObject:

    def __init__(self, vertices: list, indices: list, colors: list=None):

        if not colors:
            colors = [1] * len(vertices)  # FIXME: bad.
        colors = np.array(colors, dtype="float32")

        self.quadsCount = len(indices)

        self.__genVertexBuffer(vertices)
        self.__genIndicesBuffer(indices)
        self.__genColorBuffer(colors)
    
    def __genVertexBuffer(self, vertices):
        self.vertexBuffer = VBO()
        self.vertexBuffer.setData(np.array(vertices, dtype="float32"), 3)
    
    def __genIndicesBuffer(self, indices):
        self.indicesBuffer = IBO()
        self.indicesBuffer.setIndices(np.array(indices, dtype="byte"), len(indices))
    
    def __genColorBuffer(self, colors):
        self.colorBuffer = VBO()
        self.colorBuffer.setData(np.array(colors, dtype="float32"), 3)
    
    def render(self):
        self.vertexBuffer.setSlot(0)
        self.colorBuffer.setSlot(1)

        self.indicesBuffer.render()

        self.vertexBuffer.disable()
        self.colorBuffer.disable()

        self.indicesBuffer.unbind()
