from src.process.Game import Game

from src.engine.LevelReader import LevelReader


class GameFactory:

    @staticmethod
    def openLevel(levelName: str, width: int, height: int) -> Game:
        game = Game(width, height)

        LevelReader().loadLevel(game, "data/{}.pctv".format(levelName))

        return game
