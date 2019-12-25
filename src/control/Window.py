from OpenGL.GL import *
from pygame.locals import *
import pygame as pg


class Window:
    
    def __init__(self, size):
        pg.init()
        pg.display.set_mode(size, DOUBLEBUF|OPENGL)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)
        glClearColor(0.8, 0.8, 1, 1)
    
    def update(self):
        pg.display.flip()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    def __del__(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        pg.quit()
