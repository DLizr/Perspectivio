import pygame as pg

from src.input.IKeyboardHandler import IKeyboardHandler
from src.engine.Game import Game


class GameKeyboardHandler(IKeyboardHandler):
    
    def __init__(self, game: Game):
        self.__game = game
    
    # Override
    def handleKeys(self, keys: set):
        dX, dY, dZ = 0, 0, 0
        for key in keys:
            if key == pg.K_LEFT:
                dX += 0.05
            elif key == pg.K_RIGHT:
                dX -= 0.05
            elif key == pg.K_UP:
                dZ += 0.05
            elif key == pg.K_DOWN:
                dZ -= 0.05
        if any({dX, dY, dZ}):
            self.__game.move("Player", dX, dY, dZ)
