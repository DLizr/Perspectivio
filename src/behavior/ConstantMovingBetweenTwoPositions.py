class ConstantMovingBetweenTwoPositions:

    def __init__(self, startPos, endPos, timeBetween):
        self.__startPos = startPos
        self.__currentPos = startPos
        self.__endPos = endPos
        self.__motion = ((endPos[0] - startPos[0]) / timeBetween, 
                         (endPos[1] - startPos[1]) / timeBetween, 
                         (endPos[2] - startPos[2]) / timeBetween)
        self.__direction = 1
    
    def update(self, obj, world):
        x, y, z = self.__motion
        world.moveDynamicObject(obj, x, y, z)

        pos = obj.getPosition()
        if pos == self.__endPos or pos == self.__startPos:
            self.__direction *= -1
