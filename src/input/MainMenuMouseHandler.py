from src.input.IMouseHandler import IMouseHandler
from src.input.Button import Button


class MainMenuMouseHandler(IMouseHandler):
    
    def __init__(self, menu):
        self.__menu = menu
        self.__buttons = set()
    
    def addButton(self, x1, y1, x2, y2, name, idleAction, clickAction, hoveringAction):
        self.__buttons.add(Button(x1, y1, x2, y2, name, idleAction, clickAction, hoveringAction))
    
    def clearButtons(self):
        self.__buttons.clear()
    
    def handleClick(self, pos):
        for i in self.__buttons:
            if i.collidesPoint(*pos):
                i.onClick()
                return
    
    def handleHovering(self, pos):
        for i in self.__buttons:
            if i.collidesPoint(*pos):
                i.onHover()
            else:
                i.idle()
