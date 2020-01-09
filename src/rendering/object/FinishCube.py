from src.rendering.object.StaticCube import StaticCube


class FinishCube(StaticCube):

    def __init__(self, centerPosition: list, width):
        super().__init__(centerPosition, width, colors=[0, 1, 0] * 8)
