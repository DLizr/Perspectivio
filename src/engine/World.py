from src.engine.Field import Field
from src.engine.CollisionChecker import CollisionChecker

from src.rendering.Scene import Scene

import numpy as np


class World:
    cubeWidth = 2
   
    def __init__(self, width: int, height: int, depth: int):
        self.__field = Field(width, height, depth)
        self.__scene = Scene()
    
    def addObject(self, x: int, y: int, z: int, obj):
        self.__field.placeObject(x // self.cubeWidth, y // self.cubeWidth, z // self.cubeWidth, obj)
        self.__scene.putObject(obj)
    
    def addDynamicObject(self, x: int, y: int, z: int, obj, name: str):
        self.__field.placeObject(x // self.cubeWidth, y // self.cubeWidth, z // self.cubeWidth, obj)
        self.__scene.putDynamicObject(name, obj)
    
    def moveDynamicObject(self, name: str, dX: float, dY: float, dZ: float):
        """Collision isn't checked!"""
        obj = self.__scene.getDynamicObject(name)

        pos = obj.getPosition()
        newPos = pos + (dX, dY, dZ)

        if newPos.min() < 0:
            return

        fieldPos = (pos // self.cubeWidth).astype(int)
        newFieldPos = newPos.astype(int) // self.cubeWidth

        if not self.__field.canMoveTo(*newFieldPos):
            return

        self.__field.moveObject(*fieldPos, *newFieldPos)
        obj.moveX(dX) if dX else 0
        obj.moveY(dY) if dY else 0
        obj.moveZ(dZ) if dZ else 0

        return True

    def getObjectsColliding(self, name: str, ignoreX=False, ignoreY=False, ignoreZ=False):
        objects = set()
        obj = self.__scene.getDynamicObject(name)

        pos = obj.getPosition()
        fieldPos = pos.astype(int) // self.cubeWidth

        for i in self.__field.getTilesNearby(*fieldPos, ignoreX=ignoreX, ignoreY=ignoreY, ignoreZ=ignoreZ):
            if not i or i == obj:
                continue
            if CollisionChecker.checkCollision(obj, i, ignoreX, ignoreY, ignoreZ):
                objects.add(i)

        return objects
    
    def checkIfObjectIsFloating(self, name, ignoreX=False, ignoreY=False, ignoreZ=False):
        obj = self.__scene.getDynamicObject(name)

        pos = obj.getPosition()
        fieldPos = pos.astype(int) // self.cubeWidth

        for i in self.__field.getTilesUnder(*fieldPos, ignoreX=ignoreX, ignoreY=ignoreY, ignoreZ=ignoreZ):
            if not i:
                continue
            if CollisionChecker.checkTouch(obj, i, ignoreX, ignoreY, ignoreZ):
                return False
        
        return True
    
    def getScene(self) -> Scene:
        return self.__scene
    
    def getField(self) -> Field:
        return self.__field
    
    def render(self):
        self.__scene.render()
