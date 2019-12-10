import numpy as np

from OpenGL.GL import *


class IBO:

    def __init__(self):
        self.__indexCount = 0
        self.__id = glGenBuffers(1)
    
    def __del__(self):
        glDeleteBuffers(1, [self.__id])
    
    def bind(self):
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.__id)
    
    @staticmethod
    def unbind():
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)
    
    def setIndices(self, indices: np.ndarray, indexCount: int):
        self.bind()
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices, GL_STATIC_DRAW)
        self.__indexCount = indexCount
        self.unbind()
    
    def render(self):
        """------------------------
        Don't forget to bind a VBO!
        ------------------------"""
        self.bind()
        glDrawElements(GL_QUADS, 24, GL_UNSIGNED_BYTE, None)
        self.unbind()
