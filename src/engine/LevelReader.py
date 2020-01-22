from src.process.Game import Game

from src.engine.LevelDecryptor import LevelDecryptor


class LevelReader:

    def loadLevel(self, game: Game, filename: str):
        self.filename = filename
        with open(filename, encoding="utf-8") as file:
            self.n = 0
            for line in file.readlines():
                self.n += 1
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                try:
                    LevelDecryptor.placeObjectFromArgs(line.split(), game)
                except IOError as e:
                    raise IOError("File {}; line {}; reading error: {}".format(filename, self.n, str(e)))
