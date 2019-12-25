from src.control.Window import Window

from src.engine.Game import Game
from src.engine.LevelReader import LevelReader


class Application:
    
    def __init__(self, width: int, height: int):
        self.__window = Window((width, height))
        self.__process = Game(width, height)
        LevelReader().loadLevel(self.__process, "data/test.pctv")  # FIXME: Demo mode.

        try:
            self.mainLoop()
        except InterruptedError:  # Application is closed.
            self.terminate()
    
    def mainLoop(self):
        while True:
            self.__process.render()
            self.__window.update()
    
    def terminate(self):
        del self.__window
        del self.__process
