import numpy as np
import pyrr


class Camera:
    
    def __init__(self, x: float, y: float, z: float):
        self.__x = x
        self.__y = y
        self.__z = z
        self.__projectionMatrix: np.ndarray = None
        self.__orthogonalMatrix: np.ndarray = None
        self.__target = np.array([2, 2, 2], dtype="float32")
    
    def setProjectionMatrix(self, FOV: int, width: int, height: int, near: float, far: float):
        self.__projectionMatrix = np.transpose(pyrr.matrix44.create_perspective_projection(FOV, width/height, near, far))
        self.__orthogonalMatrix = np.transpose(pyrr.matrix44.create_orthogonal_projection_matrix(0, width, 0, height, -1000, 1000))
    
    def moveX(self, dX: float):
        self.__x += dX
    
    def moveY(self, dY: float):
        self.__y += dY
    
    def moveZ(self, dZ: float):
        self.__z += dZ
    
    def getViewMatrix(self) -> np.ndarray:
        return np.transpose(pyrr.matrix44.create_look_at(self.getEye(), self.getTarget(), np.array([0, 1, 0], dtype="float32")))
    
    def getProjectionMatrix(self) -> np.ndarray:
        return self.__projectionMatrix
    
    def getOrthogonalMatrix(self) -> np.ndarray:
        return self.__orthogonalMatrix
    
    def getModelMatrix(self):
        translation= np.transpose(pyrr.matrix44.create_from_translation(pyrr.Vector3([3, 1, 0])))
        scale= pyrr.matrix44.create_from_scale(pyrr.Vector3([50, 50, 50]))
        return np.matmul(scale, translation)
    
    def getEye(self) -> np.ndarray:
        return np.array([self.__x, self.__y, self.__z], dtype="float32")
    
    def getTarget(self) -> np.ndarray:
        return self.__target
