class CollisionChecker:

    @staticmethod
    def checkCollision(obj1, obj2, ignoreX, ignoreY, ignoreZ) -> bool:
        if obj1.getShape() == "Cube" and obj2.getShape() == "Cube":
            return CollisionChecker.checkCollisionOfTwoCubes(obj1, obj2, ignoreX, ignoreY, ignoreZ)
        elif obj1.getShape() == "Cube" and obj2.getShape() == "Rectangle":
            return CollisionChecker.checkCollisionOfCubeAndRectangle(obj1, obj2, ignoreX, ignoreY, ignoreZ)
    
    @staticmethod
    def checkTouch(obj1, obj2, ignoreX, ignoreY, ignoreZ) -> bool:
        if obj1.getShape() == "Cube" and obj2.getShape() == "Cube":
            return CollisionChecker.checkTouchOfTwoCubes(obj1, obj2, ignoreX, ignoreY, ignoreZ)

    @staticmethod
    def checkCollisionOfTwoCubes(cube1, cube2, ignoreX, ignoreY, ignoreZ) -> bool:
        pos1 = cube1.getPosition()
        pos2 = cube2.getPosition()
        width1 = cube1.getWidth()
        width2 = cube2.getWidth()
        widthSum = (width1 + width2) / 2

        if abs(pos1[0] - pos2[0]) < widthSum or ignoreX:
            if abs(pos1[1] - pos2[1]) < widthSum or ignoreY:
                if abs(pos1[2] - pos2[2]) < widthSum or ignoreZ:
                    return True
        return False
    
    @staticmethod
    def checkCollisionOfCubeAndRectangle(cube, rect, ignoreX, ignoreY, ignoreZ) -> bool:
        pos1 = cube.getPosition()
        pos2 = rect.getPosition()
        width1 = cube.getWidth()
        width2 = rect.getWidth()
        height2 = rect.getHeight()
        widthSum = (width1 + width2) / 2
        heightSum = (width1 + height2) / 2

        if abs(pos1[0] - pos2[0]) < widthSum or ignoreX:
            if abs(pos1[1] - pos2[1]) < heightSum or ignoreY:
                if abs(pos1[2] - pos2[2]) < widthSum or ignoreZ:
                    return True
        return False
    
    @staticmethod
    def checkTouchOfTwoCubes(cube1, cube2, ignoreX, ignoreY, ignoreZ) -> bool:
        pos1 = cube1.getPosition()
        pos2 = cube2.getPosition()
        width1 = cube1.getWidth()
        width2 = cube2.getWidth()
        widthSum = (width1 + width2) / 2

        if abs(pos1[0] - pos2[0]) < widthSum or ignoreX:
            if abs(pos1[1] - pos2[1]) <= widthSum or ignoreY:
                if abs(pos1[2] - pos2[2]) < widthSum or ignoreZ:
                    return True
        return False
