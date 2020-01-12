import pygame as pg

from src.input.IKeyboardHandler import IKeyboardHandler
from src.input.IMouseHandler import IMouseHandler


class EventHandler:

    def __init__(self):
        self.__keysPressed = set()
        self.__keyboardHandler: IKeyboardHandler = None
        self.__mouseHandler: IMouseHandler = None
    
    def handleEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                raise InterruptedError("Should be handled.")
            elif event.type == pg.KEYDOWN:
                self.__keysPressed.add(event.key)
            elif event.type == pg.KEYUP:
                self.__keyUp(event.key)
            elif event.type == pg.MOUSEBUTTONDOWN:
                if self.__mouseHandler:
                    self.__mouseHandler.handleClick(event.pos)
            elif event.type == pg.MOUSEMOTION:
                if self.__mouseHandler:
                    self.__mouseHandler.handleHovering(event.pos)
        self.__handleKeyboard()
    
    def __keyUp(self, key):
        try:
            self.__keysPressed.remove(key)
        except KeyError:
            return  # Somehow the key was pressed before initialization.
    
    def setKeyboardHandler(self, handler: IKeyboardHandler):
        self.__keyboardHandler = handler
    
    def setMouseHandler(self, handler: IMouseHandler):
        self.__mouseHandler = handler
    
    def __handleKeyboard(self):
        if self.__keyboardHandler:
            self.__keyboardHandler.handleKeys(self.__keysPressed)
    
    def getMouseHandler(self):
        return self.__mouseHandler
