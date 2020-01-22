from src.rendering.object.StaticCube import StaticCube
from src.rendering.object.DynamicCube import DynamicCube
from src.rendering.object.StaticPyramid import StaticPyramid
from src.rendering.object.Powerup import Powerup
from src.rendering.object.FinishCube import FinishCube

from src.action.powerup.RotationPowerupUp import RotationPowerupUp
from src.action.powerup.RotationPowerupX import RotationPowerupX
from src.action.powerup.RotationPowerupZ import RotationPowerupZ
from src.action.powerup.RotationPowerupX3D import RotationPowerupX3D
from src.action.powerup.RotationPowerupZ3D import RotationPowerupZ3D
from src.action.powerup.RotationPowerupInvertedX3D import RotationPowerupInvertedX3D
from src.action.powerup.RotationPowerupInvertedZ3D import RotationPowerupInvertedZ3D

from src.behavior.ConstantMovingBetweenTwoPositions import ConstantMovingBetweenTwoPositions


class LevelDecryptor:
    cubeWidth = 2

    @staticmethod
    def placeObjectFromArgs(args, game):
        if len(args) == 4:
            LevelDecryptor.__place4ArgsObject(args, game)
        elif len(args) == 8:
            LevelDecryptor.__place8ArgsObject(args, game)

    @staticmethod
    def __place4ArgsObject(args, game):
        x, y, z, name = args
        x = int(x) * LevelDecryptor.cubeWidth
        y = int(y) * LevelDecryptor.cubeWidth
        z = int(z) * LevelDecryptor.cubeWidth
        if name == "Player":
            game.placePlayer(x, y, z, DynamicCube([x, y, z], 2, [0, 0, 1] * 8))
        elif name == "Cube":
            game.placeObject(x, y, z, StaticCube([x, y, z], 2))
        elif name == "Spike":
            game.placeObject(x, y, z, StaticPyramid([x, y, z], 2))
        elif name == "RPowerupUp":
            powerup = Powerup([x, y, z], 1)
            powerup.setAction(RotationPowerupUp(powerup))
            game.placeUpdatableObject(x, y, z, powerup)
        elif name == "RPowerupX":
            powerup = Powerup([x, y, z], 1)
            powerup.setAction(RotationPowerupX(powerup))
            game.placeUpdatableObject(x, y, z, powerup)
        elif name == "RPowerupZ":
            powerup = Powerup([x, y, z], 1)
            powerup.setAction(RotationPowerupZ(powerup))
            game.placeUpdatableObject(x, y, z, powerup)
        elif name == "RPowerupX3D":
            powerup = Powerup([x, y, z], 1)
            powerup.setAction(RotationPowerupX3D(powerup))
            game.placeUpdatableObject(x, y, z, powerup)
        elif name == "RPowerupZ3D":
            powerup = Powerup([x, y, z], 1)
            powerup.setAction(RotationPowerupZ3D(powerup))
            game.placeUpdatableObject(x, y, z, powerup)
        elif name == "RPowerup-X3D":
            powerup = Powerup([x, y, z], 1)
            powerup.setAction(RotationPowerupInvertedX3D(powerup))
            game.placeUpdatableObject(x, y, z, powerup)
        elif name == "RPowerup-Z3D":
            powerup = Powerup([x, y, z], 1)
            powerup.setAction(RotationPowerupInvertedZ3D(powerup))
            game.placeUpdatableObject(x, y, z, powerup)
        elif name == "Finish":
            game.placeObject(x, y, z, FinishCube([x, y, z], 2))
        else:
            raise IOError("Unknown object name: {}".format(name))
    
    @staticmethod
    def __place8ArgsObject(args, game):
        x1, y1, z1, x2, y2, z2, time, name = args
        x1 = int(x1) * LevelDecryptor.cubeWidth
        y1 = int(y1) * LevelDecryptor.cubeWidth
        z1 = int(z1) * LevelDecryptor.cubeWidth
        x2 = int(x2) * LevelDecryptor.cubeWidth
        y2 = int(y2) * LevelDecryptor.cubeWidth
        z2 = int(z2) * LevelDecryptor.cubeWidth
        time = float(time) * 30

        if time <= 0:
            raise IOError("Time must be greater than zero.")

        if name == "MovingCube":
            cube = DynamicCube([x1, y1, z1], 2, [1, 1, 0] * 8)
            cube.addBehavior(ConstantMovingBetweenTwoPositions([x1, y1, z1], [x2, y2, z2], time))
            game.placeUpdatableObject(x1, y1, z1, cube)
        else:
            raise IOError("Unknown object name: {}".format(name))
