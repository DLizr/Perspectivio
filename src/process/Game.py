from src.engine.World import World

from src.view.Viewpoint import Viewpoint

from src.rendering.object.StaticCube import StaticCube
from src.rendering.object.DynamicCube import DynamicCube
from src.rendering.object.StaticPyramid import StaticPyramid

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
    
    def placeObject(self, x: int, y: int, z: int, name: str):
        if name == "Player":
            self.__world.addDynamicObject(x, y, z, DynamicCube([x, y, z], 2, [0, 0, 1] * 8), name)
        elif name == "Cube":
            self.__world.addObject(x, y, z, StaticCube([x, y, z], 2))
        elif name == "Spike":
            self.__world.addObject(x, y, z, StaticPyramid([x, y, z], 2))
        else:
            return  # Exception?

    def update(self):
        self.__eventHandler.handleEvents()
        self.__viewpoint.useShader()
        self.__world.render()
        self.__viewpoint.unuseShader()
    
    def move(self, name: str, dX: float, dY: float, dZ: float):
        self.__world.moveDynamicObject(name, dX, dY, dZ)
