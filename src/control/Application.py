from src.control.Window import Window
from src.control.EventHandler import EventHandler

from src.input.GameKeyboardHander import GameKeyboardHandler

from src.engine.Game import Game
from src.engine.LevelReader import LevelReader


class Application:
    
    def __init__(self, width: int, height: int):
        self.__window = Window((width, height))
        self.__game = Game(width, height)
        LevelReader().loadLevel(self.__game, "data/test.pctv")  # FIXME: Demo mode.
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
