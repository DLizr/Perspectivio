class ProcessChangedException(Exception):

    def __init__(self, newProcess):
        self.__newProcess = newProcess

    def getProcess(self):
        return self.__newProcess
