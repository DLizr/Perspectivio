import pygame as pg

from src.engine.SurfaceBlitter import SurfaceBlitter


class GUIEngine:

    def __init__(self, width: int, height: int, lives: int):
        self.__lives = lives
        self.__width = width
        self.__height = height

    def died(self):
        self.__lives -= 1
    
    def render(self):
        surface = pg.surface.Surface((self.__width, self.__height), pg.SRCALPHA)
        surface.fill((255, 255, 255, 0))
        pg.draw.circle(surface, (255, 0, 0), (self.__width - 50, 50), 20)
        pg.draw.circle(surface, (0, 0, 0), (self.__width - 50, 50), 20, 1)

        SurfaceBlitter.blit((self.__width, self.__height), surface)
