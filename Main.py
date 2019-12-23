from src.control.Application import Application


class Main:

    def __init__(self):
        self.application = Application(800, 600)


try:
    Main()
except Exception as e:
    raise e
