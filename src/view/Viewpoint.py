import numpy as np

from src.view.Camera import Camera
from src.lowlevel.Shader import Shader


class Viewpoint:

    def __init__(self, width: int, height: int):
        self.__camera = Camera(8, 6, 12)
        self.__camera.setProjectionMatrix(60, width, height, 0.01, 100)

        self.__shader = Shader()
        self.__createShaderProgram()
        self.switchTo3D()
    
    def __createShaderProgram(self):
        self.__shader.compile("src/shader/Vertex.glsl", "src/shader/Fragment.glsl")
    
    def switchTo2D(self):
        projMatrix = self.__camera.getOrthogonalMatrix()
        modelMatrix = self.__camera.getModelMatrix()
        PM = np.matmul(projMatrix, modelMatrix)
        self.__shader.setUniform("MVP", PM)
    
    def switchTo3D(self):
        viewMatrix = self.__camera.getViewMatrix()
        projMatrix = self.__camera.getProjectionMatrix()
        PV = np.matmul(projMatrix, viewMatrix)
        self.__shader.setUniform("MVP", PV)
    
    def setMatrix(self, matrix):
        self.__shader.setUniform("MVP", matrix)
    
    def useShader(self):
        self.__shader.use()
    
    def unuseShader(self):
        self.__shader.unuse()
