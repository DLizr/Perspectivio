class ConstantMovingBetweenTwoPositions:

    def __init__(self, startPos, endPos, timeBetween):
        self.__startPos = startPos
        self.__timeBetween = timeBetween
        self.__currentTime = 0
        self.__endPos = endPos
        self.__motion = ((endPos[0] - startPos[0]) / timeBetween, 
                         (endPos[1] - startPos[1]) / timeBetween, 
                         (endPos[2] - startPos[2]) / timeBetween)
        self.__direction = 1
    
    def update(self, obj, world):
        x, y, z = self.__motion
        x *= self.__direction
        y *= self.__direction
        z *= self.__direction
        self.__currentTime += 1
        world.moveDynamicObject(obj, x, y, z)

        if self.__currentTime == self.__timeBetween:
            self.__direction *= -1
            self.__currentTime = 0
