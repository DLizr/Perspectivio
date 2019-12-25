import pygame as pg

from src.input.IKeyboardHandler import IKeyboardHandler


class EventHandler:

    def __init__(self):
        self.__keysPressed = set()
        self.__keyboardHandler: IKeyboardHandler = None
    
    def handleEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                raise InterruptedError("Should be handled.")
            elif event.type == pg.KEYDOWN:
                self.__keysPressed.add(event.key)
            elif event.type == pg.KEYUP:
                self.__keyUp(event.key)
        self.__handleKeyboard()
    
    def __keyUp(self, key):
        try:
            self.__keysPressed.remove(key)
        except KeyError:
            return  # Somehow the key was pressed before initialization.
    
    def setKeyboardHandler(self, handler: IKeyboardHandler):
        self.__keyboardHandler = handler
    
    def __handleKeyboard(self):
        self.__keyboardHandler.handleKeys(self.__keysPressed)
