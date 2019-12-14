from src.rendering.object.StaticSceneObject import StaticSceneObject
from src.lowlevel.VertexBufferObject import VBO
from src.lowlevel.IndexBufferObject import IBO

import numpy as np
from OpenGL.GL import GL_LINES


class Wireframe:
    
    def __init__(self, vertices: list, indices: list, color: list):
        self.__genVertexBuffer(vertices)
        indicesCount = len(indices) // 2
        self.__genIndexBuffer(indices)
        self.__genColorBuffer(color, indicesCount)
    
    def __genVertexBuffer(self, vertices: list):
        self.vertexBuffer = VBO()
        self.vertexBuffer.setData(np.array(vertices, dtype="float32"), 3)
    
    def __genIndexBuffer(self, indices: list):
        self.indicesBuffer = IBO()
        self.indicesBuffer.setIndices(np.array(indices, dtype="byte"))
    
    def __genColorBuffer(self, color: list, count: int):
        self.colorBuffer = VBO()
        self.colorBuffer.setData(np.array(color * count, dtype="float32"), 3)
    
    def render(self):
        self.vertexBuffer.setSlot(0)
        self.colorBuffer.setSlot(1)

        self.indicesBuffer.render(GL_LINES)

        self.vertexBuffer.disable()
        self.colorBuffer.disable()

        self.indicesBuffer.unbind()
