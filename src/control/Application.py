from src.control.Window import Window
from src.control.ProcessChangedException import ProcessChangedException

from src.process.MainMenu import MainMenu


class Application:
    
    def __init__(self, width: int, height: int):
        self.__window = Window((width, height))
        self.__process = MainMenu(width, height)

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
