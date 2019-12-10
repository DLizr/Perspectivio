import numpy as np

from src.view.Camera import Camera
from src.lowlevel.Shader import Shader


class Viewpoint:

    def __init__(self, width: int, height: int):
        self.__camera = Camera(4, 4, 4)
        self.__camera.setProjectionMatrix(60, width, height, 0.01, 100)

        self.__shader = Shader()
        self.__createShaderProgram()
        self.__setShaderUniforms()
    
    def __createShaderProgram(self):
        self.__shader.compile("src/shader/Vertex.glsl", "src/shader/Fragment.glsl")
    
    def __setShaderUniforms(self):
        viewMatrix = self.__camera.getViewMatrix()
        projMatrix = self.__camera.getProjectionMatrix()
        VP = np.matmul(projMatrix, viewMatrix)
        self.__shader.setUniform("MVP", VP)
    
    def useShader(self):
        self.__shader.use()
    
    def unuseShader(self):
        self.__shader.unuse()
