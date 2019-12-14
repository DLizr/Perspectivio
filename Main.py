import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from src.engine.Game import Game
from src.rendering.object.StaticCube import StaticCube


class Main:

    def __init__(self):
        SIZE = 800, 600
        pg.display.set_mode(SIZE, DOUBLEBUF|OPENGL)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)
        glClearColor(0.8, 0.8, 1, 1)
        self.running = True
        self.initGame(*SIZE)
        self.gameLoop()
    
    def initGame(self, width, height):
        self.__game = Game(width, height)

    def gameLoop(self):
        clock = pg.time.Clock()
        while self.running:
            self.handleEvents()
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            self.render()
            pg.display.flip()
            clock.tick(30)
        else:
            pg.quit()
    
    def handleEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.__game.moveX("Player", -2)
                elif event.key == pg.K_RIGHT:
                    self.__game.moveX("Player", 2)
                elif event.key == pg.K_UP:
                    self.__game.moveZ("Player", -2)
                elif event.key == pg.K_DOWN:
                    self.__game.moveZ("Player", 2)
            
            elif event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    pass
                elif event.key == pg.K_RIGHT:
                    pass
                elif event.key == pg.K_UP:
                    pass
                elif event.key == pg.K_DOWN:
                    pass
    
    def render(self):
        self.__game.render()

pg.init()
try:
    Main()
except Exception as e:
    pg.quit()
    raise e
