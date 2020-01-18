import pygame as pg

from src.process.Process import Process

from src.control.EventHandler import EventHandler
from src.control.ProcessChangedException import ProcessChangedException

from src.input.ButtonMouseHandler import ButtonMouseHandler

from src.engine.SurfaceBlitter import SurfaceBlitter

from src.factory.GameFactory import GameFactory
from src.factory.ButtonFactory import ButtonFactory

from src.rendering.object.ButtonRenderer import ButtonRenderer


class MainMenu(Process):

    def __init__(self, width: int, height: int):
        self.__buttons = set()
        self.__size = (width, height)
        self.__eventHandler = EventHandler()
        self.__eventHandler.setMouseHandler(ButtonMouseHandler(self))
        self.__background = self.__createBackgoundSurface()

        self.__openMainScreen()
    
    def __createBackgoundSurface(self):
        surface = pg.surface.Surface(self.__size)
        img = pg.image.load("src/assets/Background.png").convert()

        surface.blit(img, (0, 0))
        
        return surface

    def update(self):
        self.__eventHandler.handleEvents()

        surface = self.__background.copy()
        for i in self.__buttons:
            i.render(surface)
        SurfaceBlitter.blit(self.__size, surface)
    
    def addButton(self, x: int, y: int, text: str, action):
        button = ButtonFactory.createButton(text, (x, y))
        width, height = button.getSize()

        self.__eventHandler.getMouseHandler().addButton(x, y, x + width, y + height, button.idle, action, button.hover)
        self.__buttons.add(button)
    
    def __openLevelSelectionScreen(self):
        self.__buttons.clear()
        self.__eventHandler.getMouseHandler().clearButtons()

        self.addButton(50, 50, "1", lambda: self.__startLevel("1"))
        self.addButton(200, 50, "2", lambda: self.__startLevel("2"))
        self.addButton(350, 50, "3", lambda: self.__startLevel("3"))
        self.addButton(500, 50, "4", lambda: self.__startLevel("4"))
        self.addButton(650, 50, "5", lambda: self.__startLevel("5"))

        self.addButton(289, 420, "Назад", self.__openMainScreen)
    
    def __openMainScreen(self):
        self.__buttons.clear()
        self.__eventHandler.getMouseHandler().clearButtons()

        self.addButton(280, 250, "Играть", self.__openLevelSelectionScreen)
        self.addButton(289, 380, "Выйти", self.exit)

    def __startLevel(self, level: str):
        game = GameFactory.openLevel(self, level, *self.__size)

        raise ProcessChangedException(game)

    @staticmethod
    def exit():
        raise InterruptedError
