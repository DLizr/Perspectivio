import pygame as pg
import os

from src.process.Process import Process

from src.control.EventHandler import EventHandler
from src.control.ProcessChangedException import ProcessChangedException

from src.input.MainMenuMouseHandler import MainMenuMouseHandler

from src.engine.SurfaceBlitter import SurfaceBlitter
from src.engine.GameFactory import GameFactory

from src.rendering.object.ButtonRenderer import ButtonRenderer


class MainMenu(Process):

    def __init__(self, width: int, height: int):
        self.__buttons = set()
        self.__size = (width, height)
        self.__eventHandler = EventHandler()
        self.__eventHandler.setMouseHandler(MainMenuMouseHandler(self))
        self.addButton(289, 250, "PlayButton", self.__openLevelSelectionScreen)

    def update(self):
        self.__eventHandler.handleEvents()

        surface = pg.surface.Surface(self.__size)
        for i in self.__buttons:
            i.render(surface)
        SurfaceBlitter.blit(self.__size, surface)
    
    def addButton(self, x: int, y: int, name: str, action):
        imgIdle = pg.image.load(os.path.join("src", "assets", name + ".png")).convert()
        imgHover = pg.image.load(os.path.join("src", "assets", name + "Hover.png")).convert()
        imgPress = pg.image.load(os.path.join("src", "assets", name + "Press.png")).convert()

        width, height = imgIdle.get_size()

        button = ButtonRenderer(name, (x, y), imgIdle, imgHover, imgPress)
        self.__eventHandler.getMouseHandler().addButton(x, y, x + width, y + height, name, button.idle, action, button.hover)
        self.__buttons.add(button)
    
    def __openLevelSelectionScreen(self):
        self.__buttons.clear()
        self.__eventHandler.getMouseHandler().clearButtons()

        self.addButton(50, 50, "1", lambda: self.__startLevel("1"))
        self.addButton(200, 50, "2", lambda: self.__startLevel("2"))
        self.addButton(350, 50, "3", lambda: self.__startLevel("3"))
        self.addButton(500, 50, "4", lambda: self.__startLevel("4"))
        self.addButton(650, 50, "5", lambda: self.__startLevel("5"))

    def __startLevel(self, level: str):
        game = GameFactory.openLevel(level, *self.__size)

        raise ProcessChangedException(game)
