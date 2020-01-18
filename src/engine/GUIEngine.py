import pygame as pg

from src.engine.SurfaceBlitter import SurfaceBlitter

from src.rendering.object.ButtonRenderer import ButtonRenderer

from src.factory.ButtonFactory import ButtonFactory


class GUIEngine:

    def __init__(self, game, width: int, height: int, lives: int):
        self.__opacity = 0
        self.__lives = lives
        self.__width = width
        self.__height = height
        self.__game = game
        self.__buttons = set()
        self.__pausedButtons = set()
        self.__running = True
        self.__pauseButton = self.__createPauseButton()
        self.__addButton(self.__width - 80, 10, "||", self.__pauseGame)
        self.__addPausedButton(20, self.__height - 100, "Меню", self.__exitTheGame)

        self.__baseSurface = pg.surface.Surface((width, height), pg.SRCALPHA)
    
    def __createPauseButton(self):
        button = self.__createButton(self.__width - 80, 10, "||", self.__pauseGame)
        self.__buttons.add(button)
        return button
    
    def render(self):
        surface = self.__baseSurface.copy()
        if self.__running:
            if self.__lives > 0:
                self.__drawLife(surface, 30, 40)
                if self.__lives > 1:
                    self.__drawLife(surface, 80, 40)
                    if self.__lives > 2:
                        self.__drawLife(surface, 130, 40)

        for i in self.__buttons:
            i.render(surface)
        
        if self.__game.isPaused():
            for i in self.__pausedButtons:
                i.render(surface)
            if self.__running:
                self.__pauseButton.click()
                self.__pauseButton.render(surface)
        
        SurfaceBlitter.blit((self.__width, self.__height), surface)
    
    def __drawLife(self, surface, x: int, y: int):
        pg.draw.polygon(surface, (255, 0, 0), [(x - 20, y), (x, y - 20), (x + 20, y), (x, y + 20)])
        pg.draw.polygon(surface, (0, 0, 0), [(x - 20, y), (x, y - 20), (x + 20, y), (x, y + 20)], 1)
    
    def __createButton(self, x: int, y: int, text: str, action):
        eventHandler = self.__game.getEventHandler()

        button = ButtonFactory.createButton(text, (x, y))
        width, height = button.getSize()

        eventHandler.getMouseHandler().addButton(x, y, x + width, y + height, button.idle, action, button.hover)

        return button
    
    def __addButton(self, x: int, y: int, text: str, action):
        self.__buttons.add(self.__createButton(x, y, text, action))
    
    def __addPausedButton(self, x: int, y: int, text: str, action):
        self.__pausedButtons.add(self.__createButton(x, y, text, action))

    def died(self):
        self.__lives -= 1
        
    def __pauseGame(self):
        if self.__game.isPaused():
            self.__baseSurface = pg.surface.Surface((self.__width, self.__height), pg.SRCALPHA)
            self.__game.unpause()
        else:
            self.__baseSurface.fill((255, 255, 255, 150))
            self.__game.pause()
    
    def __exitTheGame(self):
        if self.__game.isPaused():
            self.__game.quit()
    
    def __gameOver(self, timeSpent):
        self.__running = False
        self.__pauseGame()
        self.__buttons.clear()

        font = pg.font.Font("src/assets/ComicSansMS.ttf", 40)

        text = font.render("Затрачено жизней: {}".format(3 - self.__lives), 1, (0, 0, 150))
        self.__baseSurface.blit(text, (50, 120))

        time = self.__getTime(int(timeSpent))
        text = font.render("Время: {}".format(time), 1, (0, 0, 150))
        self.__baseSurface.blit(text, (50, 180))
    
    def win(self, timeSpent):
        self.__gameOver(timeSpent)

        font = pg.font.Font("src/assets/ComicSansMS.ttf", 60)

        text = font.render("Уровень пройден", 1, (0, 0, 0))
        self.__baseSurface.blit(text, (100, 10))
    
    def lost(self, timeSpent):
        self.__gameOver(timeSpent)

        font = pg.font.Font("src/assets/ComicSansMS.ttf", 60)

        text = font.render("Игра окончена", 1, (0, 0, 0))
        self.__baseSurface.blit(text, (100, 10))
    
    def __getTime(self, time: int) -> str:
        hrs = time // 3600
        mins = time // 60
        secs = time & 60

        timeString = ""
        if hrs > 0:
            timeString += str(hrs).rjust(2, "0") + ":"
        timeString += str(mins).rjust(2, "0") + ":"
        timeString += str(secs).rjust(2, "0")
        
        return timeString
