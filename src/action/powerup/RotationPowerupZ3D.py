import numpy as np
import pyrr


class RotationPowerupZ3D:
    __proj = np.transpose(pyrr.matrix44.create_perspective_projection(60, 800/600, 0.1, 100))

    def __init__(self, powerup):
        self.__centerPosition = powerup.getPosition()
        self.__view: np.ndarray = None
        self.__genViewMatrix()
        self.__matrix = np.matmul(self.__proj, self.__view)
    
    def __genViewMatrix(self):
        x = self.__centerPosition[0]
        y = self.__centerPosition[1] + 8
        z = self.__centerPosition[2] - 6
        self.__view = np.transpose(pyrr.matrix44.create_look_at(np.array([x, y, z], dtype="float32"), 
                                                                np.array(self.__centerPosition, dtype="float32"), 
                                                                np.array([0, 1, 0], dtype="float32")))
    
    def onImpact(self, game):
        game.setProjectionMatrix(self.__matrix)
        game.setIgnoreXYZ(0, 0, 0)
