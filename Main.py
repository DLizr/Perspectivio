import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = [(-1, -1, -1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1), (1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)]
edges = [(0,1), (0,2), (0,3), (4,5), (4,6), (4,7), (1,5), (2,5), (3,7), (1,6), (2,7), (3,6)]
surfaces = [(0,1,6,3), (1,6,4,5), (2,5,4,7), (4,6,3,7), (0,3,7,2), (0,1,5,2)]
colors = [(1, 0, 0), (0, 1, 0), (1, 1, 0), (0, 0, 1), (1, 0, 1), (0, 1, 1)]
size = (800, 600)


def render():

    glBegin(GL_QUADS)
    
    for surface, color in zip(surfaces, colors):
        glColor3f(*color)
        for ver in surface:
            glVertex3fv(vertices[ver])
    
    glEnd()

def main():

    pg.display.set_mode(size, DOUBLEBUF|OPENGL)
    gluPerspective(60, size[0]/size[1], 0.1, 100.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    glTranslatef(0, 0, -7)
    left, right, up, down, z, x = [False] * 6
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit(0)

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    left = True
                elif event.key == pg.K_RIGHT:
                    right = True
                elif event.key == pg.K_UP:
                    up = True
                elif event.key == pg.K_DOWN:
                    down = True
                elif event.key == pg.K_z:
                    z = True
                elif event.key == pg.K_x:
                    x = True

            elif event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    left = False
                elif event.key == pg.K_RIGHT:
                    right = False
                elif event.key == pg.K_UP:
                    up = False
                elif event.key == pg.K_DOWN:
                    down = False
                elif event.key == pg.K_z:
                    z = False
                elif event.key == pg.K_x:
                    x = False
        
        if left:
            glRotatef(-1, 0, 1, 0)
        if right:
            glRotatef(1, 0, 1, 0)
        if up:
            glRotatef(-1, 1, 0, 0)
        if down:
            glRotatef(1, 1, 0, 0)
        if z:
            glTranslatef(0, 0, 0.1)
        if x:
            glTranslatef(0, 0, -0.1)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        render()
        pg.display.flip()
        pg.time.wait(1)


pg.init()
try:
    main()
except Exception as e:
    print(e)
    pg.quit()
