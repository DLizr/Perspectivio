from OpenGL.GL import *
from pygame.locals import *
import pygame as pg


class Window:
    
    def __init__(self, size):
        pg.init()
        pg.display.set_mode(size, DOUBLEBUF|OPENGL)
        glClearColor(0.8, 0.8, 1, 1)
        self.clock = pg.time.Clock()

    @staticmethod
    def enableDepthTesting():
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
    
    def update(self):
        pg.display.flip()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        self.clock.tick(30)
    
    def __del__(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        pg.quit()
