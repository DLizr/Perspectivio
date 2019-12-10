from src.engine.Field import Field
from src.rendering.Scene import Scene


class World:
   
    def __init__(self, width: int, height: int, depth: int):
        self.__field = Field(width, height, depth)
        self.__scene = Scene()
    
    def addObject(self, x: int, y: int, z: int, obj):
        self.__field.placeObject(x, y, z, obj)
        self.__scene.putObject(obj)
    
    def addDynamicObject(self, x: int, y: int, z: int, obj, name: str):
        self.__field.placeObject(x, y, z, obj)
        self.__scene.putDynamicObject(name, obj)
    
    def getScene(self):
        return self.__scene
    
    def getField(self):
        return self.__field
    
    def render(self):
        self.__scene.render()
