import pygame as pg

from src.engine.SurfaceBlitter import SurfaceBlitter

from src.rendering.object.ButtonRenderer import ButtonRenderer


class GUIEngine:

    def __init__(self, game, width: int, height: int, lives: int):
        self.__opacity = 0
        self.__lives = lives
        self.__width = width
        self.__height = height
        self.__game = game
        self.__buttons = set()
        self.__addButton(self.__width - 60, 10, "Pause", self.__pauseGame)

    def died(self):
        self.__lives -= 1
    
    def render(self):
        surface = pg.surface.Surface((self.__width, self.__height), pg.SRCALPHA)
        surface.fill((255, 255, 255, self.__opacity))
        if self.__lives > 0:
            self.__drawLife(surface, 30, 40)
            if self.__lives > 1:
                self.__drawLife(surface, 80, 40)
                if self.__lives > 2:
                    self.__drawLife(surface, 130, 40)
        
        for i in self.__buttons:
            i.render(surface)
        
        SurfaceBlitter.blit((self.__width, self.__height), surface)
    
    def __drawLife(self, surface, x: int, y: int):
        pg.draw.polygon(surface, (255, 0, 0), [(x - 20, y), (x, y - 20), (x + 20, y), (x, y + 20)])
        pg.draw.polygon(surface, (0, 0, 0), [(x - 20, y), (x, y - 20), (x + 20, y), (x, y + 20)], 1)
    
    def __addButton(self, x: int, y: int, name: str, action):
        eventHandler = self.__game.getEventHandler()
        imgIdle = pg.image.load("src/assets/" + name + ".png").convert()
        imgHover = pg.image.load("src/assets/" + name + "Hover.png").convert()
        imgPress = pg.image.load("src/assets/" + name + "Press.png").convert()

        width, height = imgIdle.get_size()

        button = ButtonRenderer(name, (x, y), imgIdle, imgHover, imgPress)
        eventHandler.getMouseHandler().addButton(x, y, x + width, y + height, name, button.idle, action, button.hover)
        self.__buttons.add(button)
    
    def __pauseGame(self):
        if self.__game.isPaused():
            self.__opacity = 0
            self.__game.unpause()
        else:
            self.__opacity = 150
            self.__game.pause()
