from OpenGL.GL import *


class Shader:
    """Loads 2 shaders with loadShader() and compiles a program with compile()."""
    def __init__(self):
        self.program = glCreateProgram()
    
    def compile(self, vsStr: str, fsStr: str):
        vs = self.__loadShader(vsStr, GL_VERTEX_SHADER)
        if not vs:
            return
        
        fs = self.__loadShader(fsStr, GL_FRAGMENT_SHADER)
        if not fs:
            return
        
        glAttachShader(self.program, vs)
        glAttachShader(self.program, fs)
        glLinkProgram(self.program)
        error = glGetProgramiv(self.program, GL_LINK_STATUS)
        glDeleteShader(vs)
        glDeleteShader(fs)
        if error != GL_TRUE:
            info = glGetShaderInfoLog(self.program)
            raise Exception(info)
    
    def __loadShader(self, filename: str, shaderType: int) -> int:
        shaderFile = self.getFileContent(filename)
        shader = glCreateShader(shaderType)
        glShaderSource(shader, shaderFile)
        glCompileShader(shader)
        error = glGetShaderiv(shader, GL_COMPILE_STATUS)
        if error != GL_TRUE:
            info = glGetShaderInfoLog(shader)
            glDeleteShader(shader)
            raise Exception(info)
        return shader
    
    def setUniform(self, name: str, value):
        self.use()
        mId = glGetUniformLocation(self.program, name)
        glUniformMatrix4fv(mId, 1, GL_TRUE, value)
        self.unuse()
    
    def use(self):
        glUseProgram(self.program)
    
    def unuse(self):
        glUseProgram(0)
    
    @staticmethod
    def getFileContent(filename: str):
        with open(filename, encoding="utf-8") as file:
            return file.read()