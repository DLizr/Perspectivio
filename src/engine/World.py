from src.engine.Field import Field
from src.engine.CollisionChecker import CollisionChecker

from src.rendering.Scene import Scene


class World:
    cubeWidth = 2
   
    def __init__(self, width: int, height: int, depth: int):
        self.__field = Field(width, height, depth)
        self.__scene = Scene()
    
    def addObject(self, x: int, y: int, z: int, obj):
        self.__field.placeObject(obj, x // self.cubeWidth, y // self.cubeWidth, z // self.cubeWidth)
        self.__scene.putObject(obj)
    
    def addDynamicObject(self, x: int, y: int, z: int, obj, name: str):
        self.__field.placeDynamicObject(obj, x // self.cubeWidth, y // self.cubeWidth, z // self.cubeWidth)
        self.__scene.putDynamicObject(name, obj)
    
    def addUpdatableObject(self, x: int, y: int, z: int, obj):
        self.__field.placeObject(obj, x // self.cubeWidth, y // self.cubeWidth, z // self.cubeWidth)
        self.__scene.putUpdatableObject(obj)
    
    def moveDynamicObject(self, nameOrObject, dX: float, dY: float, dZ: float):
        """Collision isn't checked!"""
        if type(nameOrObject) == str:
            obj = self.__scene.getDynamicObject(nameOrObject)
        else:
            obj = nameOrObject

        pos = obj.getPosition()
        newPos = pos + (dX, dY, dZ)

        if newPos.min() < 0:
            return

        newFieldPos = newPos.astype(int) // self.cubeWidth

        self.__field.moveObject(obj, *newFieldPos)
        obj.moveX(dX) if dX else 0
        obj.moveY(dY) if dY else 0
        obj.moveZ(dZ) if dZ else 0
    
    def teleportDynamicObject(self, name: str, x: int, y: int, z: int):
        obj = self.__scene.getDynamicObject(name)

        pos = obj.getPosition()
        if x < 0:
            x = pos[0]
        if y < 0:
            y = pos[1]
        if z < 0:
            z = pos[2]

        self.__field.moveObject(obj, x // self.cubeWidth, y // self.cubeWidth, z // self.cubeWidth)

        dX = x - pos[0]
        dY = y - pos[1]
        dZ = z - pos[2]

        obj.moveX(dX) if dX else 0
        obj.moveY(dY) if dY else 0
        obj.moveZ(dZ) if dZ else 0

    def getObjectsColliding(self, name: str, ignoreX=False, ignoreY=False, ignoreZ=False) -> set:
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
    
    def getObjectsUnder(self, name, ignoreX=False, ignoreY=False, ignoreZ=False) -> set:
        objects = set()
        obj = self.__scene.getDynamicObject(name)

        pos = obj.getPosition()
        fieldPos = pos.astype(int) // self.cubeWidth

        for i in self.__field.getTilesUnder(*fieldPos, ignoreX=ignoreX, ignoreY=ignoreY, ignoreZ=ignoreZ):
            if not i or i == obj:
                continue
            if CollisionChecker.checkTouch(obj, i, ignoreX, ignoreY, ignoreZ):
                objects.add(i)
        
        return objects

    def isOutOfTheWorld(self, name: str) -> bool:
        obj = self.__scene.getDynamicObject(name)
        y = obj.getPosition()[1]
        if y <= 1 * self.cubeWidth:
            return True
        return False

    def updateObjects(self):
        for i in self.__scene.getUpdatableObjects():
            i.update(self)
    
    def getScene(self) -> Scene:
        return self.__scene
    
    def getField(self) -> Field:
        return self.__field
    
    def getSize(self) -> tuple:
        x, y, z = self.__field.getSize()
        return (x * self.cubeWidth, y * self.cubeWidth, z * self.cubeWidth)
    
    def render(self):
        self.__scene.render()
