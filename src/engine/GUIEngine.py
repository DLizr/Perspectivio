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
        if self.__lives > 0:
            self.__drawLife(surface, 30, 40)
            if self.__lives > 1:
                self.__drawLife(surface, 80, 40)
                if self.__lives > 2:
                    self.__drawLife(surface, 130, 40)

        SurfaceBlitter.blit((self.__width, self.__height), surface)
    
    def __drawLife(self, surface, x: int, y: int):
        pg.draw.polygon(surface, (255, 0, 0), [(x - 20, y), (x, y - 20), (x + 20, y), (x, y + 20)])
        pg.draw.polygon(surface, (0, 0, 0), [(x - 20, y), (x, y - 20), (x + 20, y), (x, y + 20)], 1)
