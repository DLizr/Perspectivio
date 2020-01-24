class Button:

    def __init__(self, x1, y1, x2, y2, idleAction, clickAction, hoveringAction):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.idle = idleAction
        self.onClick = clickAction
        self.onHover = hoveringAction
    
    def onClick(self):
        raise NotImplementedError

    def idle(self):
        raise NotImplementedError

    def onHover(self):
        raise NotImplementedError
    
    def collidesPoint(self, x, y) -> bool:
        return ((self.__x1 < x < self.__x2 or self.__x2 < x < self.__x1) and
                (self.__y1 < y < self.__y2 or self.__y2 < y < self.__y1))
