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
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, size[0], size[1], 0, GL_RGBA, GL_UNSIGNED_BYTE, image)

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
        glDeleteTextures(texid)
        glEnable(GL_DEPTH_TEST)
