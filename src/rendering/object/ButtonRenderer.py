class ButtonRenderer:

    def __init__(self, pos, imageIdle, imageHovering, imageClicked):
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
    
    def getSize(self) -> tuple:
        return self.__currentImage.get_size()
    
    def render(self, surface):
        surface.blit(self.__currentImage, self.__pos)
