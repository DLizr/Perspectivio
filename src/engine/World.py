from src.engine.Field import Field
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
        pos = obj.getPosition().astype(int)
        fieldPos = pos // self.cubeWidth
        newFieldPos = (pos + (dX, dY, dZ)) // self.cubeWidth

        if not np.array_equal(fieldPos, newFieldPos) and not self.__field.canMoveTo(*newFieldPos):
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
