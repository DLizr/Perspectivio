from src.engine.World import World

from src.view.Viewpoint import Viewpoint

from src.rendering.object.StaticCube import StaticCube
from src.rendering.object.DynamicCube import DynamicCube
from src.rendering.object.StaticPyramid import StaticPyramid
from src.rendering.object.Powerup import Powerup
from src.rendering.object.FinishCube import FinishCube

from src.action.powerup.RotationPowerupUp import RotationPowerupUp
from src.action.powerup.RotationPowerupX import RotationPowerupX
from src.action.powerup.RotationPowerupZ import RotationPowerupZ

from src.input.GameKeyboardHander import GameKeyboardHandler

from src.control.EventHandler import EventHandler

from src.process.Process import Process
# TODO: import GUI engine.


class Game(Process):

    def __init__(self, width: int, height: int):
        self.__viewpoint = Viewpoint(width, height)
        self.__world = World(5, 5, 5)
        self.__eventHandler = EventHandler()
        self.__eventHandler.setKeyboardHandler(GameKeyboardHandler(self))
        self.__ignoreX = False
        self.__ignoreY = False
        self.__ignoreZ = False
        self.__movement = [0, 0, 0]

        self.__spawnpoint: list = None
        self.__lives = 3
    
    def placeObject(self, x: int, y: int, z: int, name: str):
        if name == "Player":
            self.__world.addDynamicObject(x, y, z, DynamicCube([x, y, z], 2, [0, 0, 1] * 8), name)
            self.__spawnpoint = [x, y, z]
        elif name == "Cube":
            self.__world.addObject(x, y, z, StaticCube([x, y, z], 2))
        elif name == "Spike":
            self.__world.addObject(x, y, z, StaticPyramid([x, y, z], 2))
        elif name == "RPowerupUp":
            powerup = Powerup([x, y, z], 2)
            powerup.setAction(RotationPowerupUp(powerup))
            self.__world.addDynamicObject(x, y, z, powerup, name)
        elif name == "RPowerupX":
            powerup = Powerup([x, y, z], 2)
            powerup.setAction(RotationPowerupX(powerup))
            self.__world.addDynamicObject(x, y, z, powerup, name)
        elif name == "RPowerupZ":
            powerup = Powerup([x, y, z], 2)
            powerup.setAction(RotationPowerupZ(powerup))
            self.__world.addDynamicObject(x, y, z, powerup, name)
        elif name == "Finish":
            self.__world.addObject(x, y, z, FinishCube([x, y, z], 2))
        else:
            return  # Exception?

    def update(self):
        self.__eventHandler.handleEvents()
        self.__moveObjects()
        self.__viewpoint.useShader()
        self.__world.render()
        self.__viewpoint.unuseShader()

    def move(self, dX: float, dY: float, dZ: float):
        self.__movement = [dX, dY, dZ]

    def __moveObjects(self):
        self.__movePlayer()
        self.__gravity("Player")
    
    def __movePlayer(self):
        if not any(self.__movement):
            return
        dX, dY, dZ = self.__movement
        self.__world.moveDynamicObject("Player", dX, dY, dZ)
        objectsCollided = self.__world.getObjectsColliding("Player", ignoreX=self.__ignoreX, ignoreY=self.__ignoreY, ignoreZ=self.__ignoreZ)
        if self.__checkCollidedObjects(objectsCollided):
            self.__world.moveDynamicObject("Player", -dX, -dY, -dZ)

    def __checkCollidedObjects(self, objects):
        cantMove = False
        for i in objects:
            if type(i) == StaticPyramid:
                self.__died()
            elif type(i) == StaticCube:
                cantMove = True and not self.__ignoreY
            elif type(i) == Powerup:
                i.onImpact(self)
            elif type(i) == FinishCube:
                print("You Win!")  # Call to Application.
                cantMove = True and not self.__ignoreY

        return cantMove
    
    def __died(self):
        if self.__lives == 0:
            print("You already lost.")  # Call to Application.
            return
        else:
            self.__world.teleportDynamicObject("Player", *self.__spawnpoint)
            self.__lives -= 1

    def __gravity(self, name: str):
        isFloating = self.__world.checkIfObjectIsFloating("Player", ignoreX=self.__ignoreX, ignoreY=self.__ignoreY, ignoreZ=self.__ignoreZ)
        if not isFloating:
            return
        if self.__world.isOutOfTheWorld(name):
            self.__died()
        else:
            self.__world.moveDynamicObject(name, 0, -0.1, 0)
    
    def setProjectionMatrix(self, matrix):
        self.__viewpoint.setMatrix(matrix)
    
    def setIgnoreXYZ(self, ignoreX, ignoreY, ignoreZ):
        self.__ignoreX = bool(ignoreX)
        self.__ignoreY = bool(ignoreY)
        self.__ignoreZ = bool(ignoreZ)
