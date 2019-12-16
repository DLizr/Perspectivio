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
        self.x, self.y, self.z = 0, 0, 0
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
                    self.x = 0.1
                elif event.key == pg.K_RIGHT:
                    self.x = -0.1
                elif event.key == pg.K_UP:
                    self.z = 0.1
                elif event.key == pg.K_DOWN:
                    self.z = -0.1
            
            elif event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    self.x = 0
                elif event.key == pg.K_RIGHT:
                    self.x = 0
                elif event.key == pg.K_UP:
                    self.z = 0
                elif event.key == pg.K_DOWN:
                    self.z = 0

        if any((self.x, self.y, self.z)):
            self.__game.move("Player", self.x, self.y, self.z)
    
    def render(self):
        self.__game.render()

pg.init()
try:
    Main()
except Exception as e:
    pg.quit()
    raise e
