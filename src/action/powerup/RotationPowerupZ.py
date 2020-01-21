import numpy as np
import pyrr


class RotationPowerupZ:
    __ortho = np.transpose(pyrr.matrix44.create_orthogonal_projection_matrix(0, 800, 0, 600, -1000, 1000))

    def __init__(self, powerup):
        self.__centerPosition = powerup.getPosition()
        self.__model: np.ndarray = None
        self.__genModelMatrix()
        self.__matrix = np.matmul(self.__ortho, self.__model)
    
    def __genModelMatrix(self):
        dX = 8 - self.__centerPosition[0]
        dY = 6 - self.__centerPosition[1]
        translation = np.transpose(pyrr.matrix44.create_from_translation(np.array([dX, dY, 0])))
        scale = pyrr.matrix44.create_from_scale(np.array([50, 50, 50]))
        ST = np.matmul(scale, translation)
        self.__model = ST
    
    def onImpact(self, game):
        game.setProjectionMatrix(self.__matrix)
        if game.getIgnoreXYZ() != (0, 0, 1):
            game.teleportPlayer(*self.__centerPosition)
        game.setIgnoreXYZ(0, 0, 1)
