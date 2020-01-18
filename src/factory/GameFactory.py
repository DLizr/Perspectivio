from src.process.Game import Game

from src.engine.LevelReader import LevelReader


class GameFactory:

    @staticmethod
    def openLevel(menu, levelName: str, width: int, height: int) -> Game:
        game = Game(menu, width, height)

        LevelReader().loadLevel(game, "data/{}.pctv".format(levelName))

        return game
