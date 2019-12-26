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
        self.__field.placeObject(x, y, z, obj)
        self.__scene.putObject(obj)
    
    def addDynamicObject(self, x: int, y: int, z: int, obj, name: str):
        self.__field.placeObject(x, y, z, obj)
        self.__scene.putDynamicObject(name, obj)
    
    def moveDynamicObject(self, name: str, dX: float, dY: float, dZ: float):
        obj = self.__scene.getDynamicObject(name)

        pos = obj.getPosition()
        newPos = pos + (dX, dY, dZ)

        if newPos.min() < 0:
            return

        fieldPos = (pos // self.cubeWidth).astype(int)
        newFieldPos = newPos.astype(int) // self.cubeWidth

        if not self.__field.canMoveTo(*newFieldPos):
            return
        
        dynamicCube = (*newPos, obj.getWidth())
        
        for i in self.__field.getTilesNearby(*newFieldPos):
            if not i or i == obj:
                continue
            cube = (*i.getPosition(), i.getWidth())  # TODO: If an object is not a cube?
            # FIXME: Pyramid collision raises an exception.
            if CollisionChecker.checkCollisionOfTwoCubes(dynamicCube, cube):
                return

        self.__field.moveObject(*fieldPos, *newFieldPos)
        obj.moveX(dX) if dX else 0
        obj.moveY(dY) if dY else 0
        obj.moveZ(dZ) if dZ else 0
        
    
    def getScene(self) -> Scene:
        return self.__scene
    
    def getField(self) -> Field:
        return self.__field
    
    def render(self):
        self.__scene.render()
