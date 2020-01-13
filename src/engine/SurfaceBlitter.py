from OpenGL.GL import *

import pygame as pg

import numpy as np

from src.lowlevel.VertexBufferObject import VBO


class SurfaceBlitter:

    @staticmethod
    def blit(size, surface: pg.surface.Surface):
        x1 = 0
        y1 = 0
        x2 = size[0]
        y2 = size[1]

        image = pg.image.tostring(surface, "RGBA", 1)
        glEnable(GL_TEXTURE_2D)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, size[0], size[1], 0, -1, 1)
        glDisable(GL_DEPTH_TEST)
        glMatrixMode(GL_MODELVIEW)

        texid = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texid)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, size[0], size[1], 0, GL_RGBA, GL_UNSIGNED_BYTE, image)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

        glBegin(GL_QUADS)

        glTexCoord2d(0, 0)
        glVertex3f(x1, y2, -1)

        glTexCoord2d(1, 0)
        glVertex3f(x2, y2, -1)

        glTexCoord2d(1, 1)
        glVertex3f(x2, y1, -1)

        glTexCoord2d(0, 1)
        glVertex3f(x1, y1, -1)

        glEnd()
    
    @staticmethod
    def stackOverflowBlit(x, y, img, r, g, b):
        w,h = img.get_size()
        raw_data = img.get_buffer().raw
        data = np.fromstring(raw_data, np.uint8)

        bitmap_tex = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, bitmap_tex)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA,w,h,0,GL_BGRA,GL_UNSIGNED_BYTE,data)

        # save and set model view and projection matrix
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        glOrtho(0, 800, 0, 600, -2, 2)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        # enable blending
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)

        # draw textured quad
        glColor3f(r,g,b)

        glEnable(GL_TEXTURE_2D)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 1)
        glVertex2f(x, y)
        glTexCoord2f(1, 1)
        glVertex2f(x+w, y)
        glTexCoord2f(1, 0)
        glVertex2f(x+w, y+h)
        glTexCoord2f(0, 0)
        glVertex2f(x, y+h)
        glEnd()
        glDisable(GL_TEXTURE_2D)

        # restore matrices
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()

        # disable blending
        glDisable(GL_BLEND)