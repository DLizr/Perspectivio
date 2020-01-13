import pygame as pg
import os

from src.process.Process import Process

from src.control.EventHandler import EventHandler

from src.input.MainMenuMouseHandler import MainMenuMouseHandler

from src.engine.SurfaceBlitter import SurfaceBlitter

from src.rendering.object.ButtonRenderer import ButtonRenderer


class MainMenu(Process):

    def __init__(self, width: int, height: int):
        self.__buttons = set()
        self.__size = (width, height)
        self.__eventHandler = EventHandler()
        self.__eventHandler.setMouseHandler(MainMenuMouseHandler(self))
        self.addButton(0, 0, "PlayButton", 0)

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
        self.__eventHandler.getMouseHandler().addButton(x, y, x + width, y + height, name, button.idle, self.__openLevelSelectionScreen, button.hover)
        self.__buttons.add(button)
    
    def __openLevelSelectionScreen(self):
        for i in self.__buttons:
            if i.getName() == "PlayButton":
                i.click()
                return
        print("Yay")
