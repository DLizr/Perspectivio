import pygame as pg

from src.process.Process import Process

from src.control.EventHandler import EventHandler

from src.input.MainMenuMouseHandler import MainMenuMouseHandler

from src.engine.SurfaceBlitter import SurfaceBlitter


class MainMenu(Process):

    def __init__(self, width: int, height: int):
        self.__size = (width, height)
        self.__eventHandler = EventHandler()
        self.__eventHandler.setMouseHandler(MainMenuMouseHandler(self))

    def update(self):
        self.__eventHandler.handleEvents()
