class IMouseHandler:

    def addButton(self, x1, y1, x2, y2, idleAction, clickAction, hoveringAction):
        raise NotImplementedError("Override.")

    def handleClick(self, pos):
        raise NotImplementedError("Override.")

    def handleHovering(self, pos):
        raise NotImplementedError("Override.")
