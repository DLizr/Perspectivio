import time


from src.engine.World import World
from src.engine.GUIEngine import GUIEngine

from src.view.Viewpoint import Viewpoint

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

from src.input.GameKeyboardHander import GameKeyboardHandler
from src.input.ButtonMouseHandler import ButtonMouseHandler

from src.control.EventHandler import EventHandler
from src.control.ProcessChangedException import ProcessChangedException

from src.process.Process import Process


class Game(Process):

    def __init__(self, menu, width: int, height: int):
        self.__menu = menu
        self.__viewpoint = Viewpoint(width, height)
        self.__world = World(5, 5, 5)
        self.__eventHandler = EventHandler()
        self.__eventHandler.setKeyboardHandler(GameKeyboardHandler(self))
        self.__eventHandler.setMouseHandler(ButtonMouseHandler(self))
        self.__gui = GUIEngine(self, width, height, 3)
        self.__ignoreX = False
        self.__ignoreY = False
        self.__ignoreZ = False
        self.__movement = [0, 0, 0]
        self.__size = (width, height)

        self.__spawnpoint: list = None
        self.__lives = 3
        self.__paused = False

        self.__startingTime = time.time()
        self.__viewpoint.switchTo2D()
        self.setIgnoreXYZ(0, 0, 1)
    
    def placeObject(self, x: int, y: int, z: int, name: str):
        if name == "Player":
            self.__world.addDynamicObject(x, y, z, DynamicCube([x, y, z], 2, [0, 0, 1] * 8), name)
            self.__spawnpoint = [x, y, z]
        elif name == "Cube":
            self.__world.addObject(x, y, z, StaticCube([x, y, z], 2))
        elif name == "Spike":
            self.__world.addObject(x, y, z, StaticPyramid([x, y, z], 2))
        elif name == "RPowerupUp":
            powerup = Powerup([x, y, z], 1)
            powerup.setAction(RotationPowerupUp(powerup))
            self.__world.addUpdatableObject(x, y, z, powerup)
        elif name == "RPowerupX":
            powerup = Powerup([x, y, z], 1)
            powerup.setAction(RotationPowerupX(powerup))
            self.__world.addUpdatableObject(x, y, z, powerup)
        elif name == "RPowerupZ":
            powerup = Powerup([x, y, z], 1)
            powerup.setAction(RotationPowerupZ(powerup))
            self.__world.addUpdatableObject(x, y, z, powerup)
        elif name == "RPowerupX3D":
            powerup = Powerup([x, y, z], 1)
            powerup.setAction(RotationPowerupX3D(powerup))
            self.__world.addUpdatableObject(x, y, z, powerup)
        elif name == "RPowerupZ3D":
            powerup = Powerup([x, y, z], 1)
            powerup.setAction(RotationPowerupZ3D(powerup))
            self.__world.addUpdatableObject(x, y, z, powerup)
        elif name == "RPowerup-X3D":
            powerup = Powerup([x, y, z], 1)
            powerup.setAction(RotationPowerupInvertedX3D(powerup))
            self.__world.addUpdatableObject(x, y, z, powerup)
        elif name == "RPowerup-Z3D":
            powerup = Powerup([x, y, z], 1)
            powerup.setAction(RotationPowerupInvertedZ3D(powerup))
            self.__world.addUpdatableObject(x, y, z, powerup)
        elif name == "Finish":
            self.__world.addObject(x, y, z, FinishCube([x, y, z], 2))
        else:
            return  # Exception?

    def update(self):
        self.__eventHandler.handleEvents()
        if not self.__paused:
            self.__moveObjects()
            self.__world.updateObjects()
        self.__viewpoint.useShader()
        self.__world.render()
        self.__viewpoint.unuseShader()
        self.__gui.render()

    def move(self, dX: float, dY: float, dZ: float):
        if self.__ignoreX:
            dX = 0
        if self.__ignoreZ:
            dZ = 0
        self.__movement = [dX, dY, dZ]

    def __moveObjects(self):
        self.__gravity("Player")
        self.__movePlayer()
    
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
                self.__win()
                cantMove = True and not self.__ignoreY

        return cantMove
    
    def __died(self):
        if self.__lives == 0:
            self.__lost()
            return
        else:
            self.__world.teleportDynamicObject("Player", *self.__spawnpoint)
            self.__lives -= 1
            self.__gui.died()
        
    def __lost(self):
        timeSpent = time.time() - self.__startingTime
        self.__gui.lost(timeSpent)
    
    def __win(self):
        timeSpent = time.time() - self.__startingTime
        self.__gui.win(timeSpent)

    def __gravity(self, name: str):
        objects = self.__world.getObjectsUnder("Player", ignoreX=self.__ignoreX, ignoreY=self.__ignoreY, ignoreZ=self.__ignoreZ)
        if self.__checkCollidedObjects(objects) != self.__ignoreY:
            self.__movement[1] = 0
            return
        if self.__world.isOutOfTheWorld(name):
            self.__died()
        else:
            self.__movement[1] = -0.25
    
    def setProjectionMatrix(self, matrix):
        self.__viewpoint.setMatrix(matrix)
    
    def setIgnoreXYZ(self, ignoreX, ignoreY, ignoreZ):
        self.__ignoreX = bool(ignoreX)
        self.__ignoreY = bool(ignoreY)
        self.__ignoreZ = bool(ignoreZ)
    
    def pause(self):
        self.__paused = True
    
    def unpause(self):
        self.__paused = False
    
    def isPaused(self):
        return self.__paused
    
    def quit(self):
        raise ProcessChangedException(self.__menu)
    
    def getEventHandler(self):
        return self.__eventHandler
