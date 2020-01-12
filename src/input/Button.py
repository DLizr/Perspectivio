class Button:

    def __init__(self, x1, y1, x2, y2, name, clickAction, hoveringAction):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__name = name
        self.onClick = clickAction
        self.onHover = hoveringAction
    
    def collidesPoint(self, x, y):
        return ((self.__x1 < x < self.__x2 or self.__x2 < x < self.__x1) and
                (self.__y1 < y < self.__y2 or self.__y2 < y < self.__y1))
    
    def getName(self):
        return self.__name
