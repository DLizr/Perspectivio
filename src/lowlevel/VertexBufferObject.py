import numpy as np

from OpenGL.GL import *


class VBO:
    
    def __init__(self):
        self.__componentCount = 0
        self.__slot: int = None
        self.__id = glGenBuffers(1)
    
    def __del__(self):
        glDeleteBuffers(1, [self.__id])
    
    def bind(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.__id)
    
    @staticmethod
    def unbind():
        glBindBuffer(GL_ARRAY_BUFFER, 0)
    
    def setData(self, data: np.ndarray, componentCount: int):
        self.bind()
        glBufferData(GL_ARRAY_BUFFER, data, GL_STATIC_DRAW)
        self.__componentCount = componentCount
        self.unbind()
    
    def updateData(self, data: np.ndarray):
        self.bind()
        glBufferSubData(GL_ARRAY_BUFFER, 0, data=data)
        self.unbind()
    
    def setSlot(self, slot: int):
        """---------------------
        Don't forget to disable!
        ---------------------"""
        self.__slot = slot
        glEnableVertexAttribArray(slot)
        self.bind()
        glVertexAttribPointer(slot, self.__componentCount, GL_FLOAT, GL_FALSE, 0, None)
        self.unbind()
    
    def disable(self):
        glDisableVertexAttribArray(self.__slot)
    
    def getId(self):
        return self.__id
    
    def render(self):
        self.bind()
        glDrawArrays(GL_QUADS, 0, 8)
