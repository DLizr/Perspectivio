import pygame as pg

from src.rendering.object.ButtonRenderer import ButtonRenderer


class ButtonFactory:

    @staticmethod
    def createButton(text: str, pos):
        font = pg.font.Font("src/assets/ButtonFont.otf", 70)
        textSurface = font.render(text, 1, (255, 255, 255))

        width, height = textSurface.get_size()
        background = pg.surface.Surface((width + 30, height))
        background.fill(pg.Color("#3e6483"))
        pg.draw.rect(background, pg.color.Color("#174164"), [(3, 3), (width + 23, height - 7)], 6)

        idle = background.copy()
        idle.blit(textSurface, (15, 0))

        hover = idle.copy()
        pg.draw.rect(hover, (255, 255, 255), [(3, 3), (width + 23, height - 7)], 6)

        clicked = background.copy()
        clicked.fill(pg.color.Color("#174164"))
        clicked.blit(textSurface, (15, 0))
        pg.draw.rect(clicked, (255, 255, 255), [(3, 3), (width + 23, height - 7)], 6)

        button = ButtonRenderer("", pos, idle, hover, clicked)
        return button
