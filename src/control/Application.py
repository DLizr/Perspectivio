from src.control.Window import Window
from src.control.EventHandler import EventHandler
from src.input.GameKeyboardHander import GameKeyboardHandler
from src.engine.Game import Game


class Application:
    
    def __init__(self, width: int, height: int):
        self.__window = Window((width, height))
        self.__game = Game(width, height)
        self.__eventHandler = EventHandler()
        self.__eventHandler.setKeyboardHandler(GameKeyboardHandler(self.__game))

        try:
            self.mainLoop()
        except InterruptedError:  # Application is closed.
            self.terminate()
    
    def mainLoop(self):
        while True:
            self.__eventHandler.handleEvents()
            self.__game.render()
            self.__window.update()
    
    def terminate(self):
        del self.__window
        del self.__game
