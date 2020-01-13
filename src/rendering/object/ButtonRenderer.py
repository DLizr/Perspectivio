class ButtonRenderer:

    def __init__(self, name, pos, imageIdle, imageHovering, imageClicked):
        self.__name = name
        self.__pos = pos
        self.__imageIdle = imageIdle
        self.__imageHovering = imageHovering
        self.__imageClicked = imageClicked
        self.__currentImage = imageIdle
    
    def hover(self):
        self.__currentImage = self.__imageHovering
    
    def click(self):
        self.__currentImage = self.__imageClicked
    
    def idle(self):
        self.__currentImage = self.__imageIdle
    
    def render(self, surface):
        surface.blit(self.__currentImage, self.__pos)
    
    def getName(self):
        return self.__name
