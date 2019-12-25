from src.engine.World import World

from src.view.Viewpoint import Viewpoint

from src.rendering.object.StaticCube import StaticCube
from src.rendering.object.DynamicCube import DynamicCube

from src.input.GameKeyboardHander import GameKeyboardHandler

from src.control.EventHandler import EventHandler

from src.process.Process import Process
# TODO: import GUI engine.


class Game(Process):
    isDynamic = {"Player": True, "Cube": False}

    def __init__(self, width: int, height: int):
        self.__viewpoint = Viewpoint(width, height)
        self.__world = World(5, 5, 5)
        self.__eventHandler = EventHandler()
        self.__eventHandler.setKeyboardHandler(GameKeyboardHandler(self))
    
    def placeObject(self, x: int, y: int, z: int, name: str):
        try:
            if self.isDynamic[name]:
                self.__world.addDynamicObject(x, y, z, DynamicCube([x, y, z], 2, [0, 0, 1] * 8), name)
            else:
                self.__world.addObject(x, y, z, StaticCube([x, y, z], 2))
        
        except KeyError:
            return  # TODO: Idk what to do.

    def update(self):
        self.__eventHandler.handleEvents()
        self.__viewpoint.useShader()
        self.__world.render()
        self.__viewpoint.unuseShader()
    
    def move(self, name: str, dX: float, dY: float, dZ: float):
        self.__world.moveDynamicObject(name, dX, dY, dZ)
