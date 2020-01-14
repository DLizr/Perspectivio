from src.control.Window import Window

from src.process.Game import Game
from src.process.MainMenu import MainMenu

from src.engine.LevelReader import LevelReader

from src.control.ProcessChangedException import ProcessChangedException


class Application:
    
    def __init__(self, width: int, height: int):
        self.__window = Window((width, height))
        self.__process = MainMenu(width, height)
        # LevelReader().loadLevel(self.__process, "data/test.pctv")  # FIXME: Demo mode.

        try:
            self.mainLoop()
        except InterruptedError:  # Application is closed.
            self.terminate()
    
    def mainLoop(self):
        while True:
            try:
                self.__process.update()
            except ProcessChangedException as e:
                self.setProcess(e.getProcess())
                self.__window.enableDepthTesting()

            self.__window.update()
    
    def terminate(self):
        del self.__process
        del self.__window
    
    def setProcess(self, process):
        del self.__process
        self.__process = process
