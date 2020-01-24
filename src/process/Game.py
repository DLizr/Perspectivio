import time


from src.engine.World import World
from src.engine.GUIEngine import GUIEngine

from src.view.Viewpoint import Viewpoint

from src.rendering.object.StaticCube import StaticCube
from src.rendering.object.DynamicCube import DynamicCube
from src.rendering.object.StaticPyramid import StaticPyramid
from src.rendering.object.Powerup import Powerup
from src.rendering.object.FinishCube import FinishCube

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
    
    def placeObject(self, x: int, y: int, z: int, obj):
        self.__world.addObject(x, y, z, obj)
    
    def placeDynamicObject(self, x: int, y: int, z: int, obj, name: str):
        self.__world.addDynamicObject(x, y, z, obj, name)
    
    def placeUpdatableObject(self, x: int, y: int, z: int, obj):
        self.__world.addUpdatableObject(x, y, z, obj)
    
    def placePlayer(self, x: int, y: int, z: int, obj):
        self.__world.addDynamicObject(x, y, z, obj, "Player")
        self.__spawnpoint = [x, y, z]

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
        stuck = False
        dX, dY, dZ = self.__movement

        objectsCollided = self.__world.getObjectsColliding("Player", ignoreX=self.__ignoreX, ignoreY=self.__ignoreY, ignoreZ=self.__ignoreZ)
        if self.__checkCollidedObjects(objectsCollided) and not self.__ignoreY:
            stuck = True

        if dX:
            self.__world.moveDynamicObject("Player", dX, 0, 0)
            objectsCollided = self.__world.getObjectsColliding("Player", ignoreX=self.__ignoreX, ignoreY=self.__ignoreY, ignoreZ=self.__ignoreZ)
            if self.__checkCollidedObjects(objectsCollided) and not self.__ignoreY:
                self.__world.moveDynamicObject("Player", -dX, 0, 0)
        
        if dY:
            self.__world.moveDynamicObject("Player", 0, dY, 0)
            objectsCollided = self.__world.getObjectsColliding("Player", ignoreX=self.__ignoreX, ignoreY=self.__ignoreY, ignoreZ=self.__ignoreZ)
            if self.__checkCollidedObjects(objectsCollided) and not self.__ignoreY and not stuck:
                self.__world.moveDynamicObject("Player", 0, -dY, 0)
        
        if dZ:
            self.__world.moveDynamicObject("Player", 0, 0, dZ)
            objectsCollided = self.__world.getObjectsColliding("Player", ignoreX=self.__ignoreX, ignoreY=self.__ignoreY, ignoreZ=self.__ignoreZ)
            if self.__checkCollidedObjects(objectsCollided) and not self.__ignoreY:
                self.__world.moveDynamicObject("Player", 0, 0, -dZ)

    def __checkCollidedObjects(self, objects) -> bool:
        cantMove = False
        for i in objects:
            if type(i) == StaticPyramid:
                self.__died()
            elif type(i) == StaticCube:
                cantMove = True
            elif type(i) == DynamicCube:
                cantMove = True
            elif type(i) == Powerup:
                i.onImpact(self)
            elif type(i) == FinishCube:
                self.__win()
                cantMove = True

        return cantMove
    
    def __died(self):
        if self.__lives == 0:
            self.__lost()
            return
        else:
            self.__world.teleportDynamicObject("Player", *self.__spawnpoint)
            self.__viewpoint.switchTo2D()
            self.setIgnoreXYZ(0, 0, 1)
            self.__lives -= 1
            self.__gui.died()
        
    def __lost(self):
        timeSpent = time.time() - self.__startingTime
        self.__gui.lost(timeSpent)
    
    def __win(self):
        timeSpent = time.time() - self.__startingTime
        self.__gui.win(timeSpent)
    
    def teleportPlayer(self, x: int, y: int, z: int):
        self.__world.teleportDynamicObject("Player", x, y, z)
    
    def playerOnTop(self):
        y = self.__world.getSize()[1]
        self.__world.teleportDynamicObject("Player", -1, y, -1)

    def __gravity(self, name: str):
        objects = self.__world.getObjectsUnder("Player", ignoreX=self.__ignoreX, ignoreY=self.__ignoreY, ignoreZ=self.__ignoreZ)
        if self.__checkCollidedObjects(objects):
            self.__movement[1] = 0
            return
        if self.__world.isOutOfTheWorld(name) or self.__ignoreY:
            self.__died()
        else:
            self.__movement[1] = -0.25
    
    def setProjectionMatrix(self, matrix):
        self.__viewpoint.setMatrix(matrix)
    
    def setIgnoreXYZ(self, ignoreX, ignoreY, ignoreZ):
        self.__ignoreX = bool(ignoreX)
        self.__ignoreY = bool(ignoreY)
        self.__ignoreZ = bool(ignoreZ)
    
    def getIgnoreXYZ(self) -> tuple:
        return int(self.__ignoreX), int(self.__ignoreY), int(self.__ignoreZ)
    
    def pause(self):
        self.__paused = True
    
    def unpause(self):
        self.__paused = False
    
    def isPaused(self):
        return self.__paused
    
    def quit(self):
        raise ProcessChangedException(self.__menu)
    
    def getEventHandler(self) -> EventHandler:
        return self.__eventHandler
