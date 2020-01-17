import pygame as pg


class ButtonFactory:

    @staticmethod
    def createButton(text: str):
        font = pg.font.Font("src/assets/ButtonFont.otf", 70)
        textSurface = font.render(text, 1, (255, 255, 255))

        width, height = textSurface.get_size()
        surface = pg.surface.Surface((width + 30, height))
        surface.fill(pg.Color("#264b69"))

        surface.blit(textSurface, (15, 0))
        return surface

