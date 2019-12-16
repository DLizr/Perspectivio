from src.engine.World import World
from src.view.Viewpoint import Viewpoint
from src.rendering.object.StaticCube import StaticCube
from src.rendering.object.DynamicCube import DynamicCube
# TODO: import GUI engine.


class Game:

    def __init__(self, width: int, height: int):
        self.__viewpoint = Viewpoint(width, height)
        self.__world = World(5, 5, 5)
        self.placeObjects()
    
    def placeObjects(self):  # FIXME: Demo mode.
        self.__world.addObject(0, 0, 0, StaticCube([0, 0, 0], 2))
        self.__world.addObject(1, 0, 0, StaticCube([2, 0, 0], 2))
        self.__world.addObject(0, 0, 1, StaticCube([0, 0, 2], 2))
        self.__world.addObject(-1, 0, 0, StaticCube([-2, 0, 0], 2))
        self.__world.addObject(0, 0, -1, StaticCube([0, 0, -2], 2))
        self.__world.addObject(2, 1, 2, StaticCube([4, 2, 4], 2))

        self.__world.addDynamicObject(0, 1, 0, DynamicCube([0, 2, 0], 2, [0, 0, 1] * 8), "Player")
    
    def render(self):
        self.__viewpoint.useShader()
        self.__world.render()
        self.__viewpoint.unuseShader()
    
    def move(self, name: str, dX: float, dY: float, dZ: float):
        self.__world.moveDynamicObject(name, dX, dY, dZ)
