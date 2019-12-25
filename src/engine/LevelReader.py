from src.process.Game import Game


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
                x, y, z, name = self.__getDataIfCorrect(line)
                game.placeObject(int(x), int(y), int(z), name)
                    
    
    def __getDataIfCorrect(self, line):
        try:
            x, y, z, name = line.split()
        except ValueError:
            raise IOError("Unable to read the file {} on line {}.".format(self.filename, self.n))
        return x, y, z, name
