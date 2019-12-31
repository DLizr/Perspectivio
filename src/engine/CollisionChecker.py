from src.rendering.object.StaticCube import StaticCube
from src.rendering.object.DynamicCube import DynamicCube
from src.rendering.object.StaticPyramid import StaticPyramid
from src.rendering.object.Powerup import Powerup


class CollisionChecker:

    @staticmethod
    def checkCollision(obj1, obj2):
        if obj1.getShape() == "Cube" and obj2.getShape() == "Cube":
            return CollisionChecker.checkCollisionOfTwoCubes(obj1, obj2)
        elif obj1.getShape() == "Cube" and obj2.getShape() == "Rectangle":
            return CollisionChecker.checkCollisionOfCubeAndRectangle(obj1, obj2)

    @staticmethod
    def checkCollisionOfTwoCubes(cube1, cube2):
        pos1 = cube1.getPosition()
        pos2 = cube2.getPosition()
        width1 = cube1.getWidth()
        width2 = cube2.getWidth()
        widthSum = (width1 + width2) / 2

        if abs(pos1[0] - pos2[0]) < widthSum:
            if abs(pos1[1] - pos2[1]) < widthSum:
                if abs(pos1[2] - pos2[2]) < widthSum:
                    return True
        return False
    
    @staticmethod
    def checkCollisionOfCubeAndRectangle(cube, rect):
        pos1 = cube.getPosition()
        pos2 = rect.getPosition()
        width1 = cube.getWidth()
        width2 = rect.getWidth()
        height2 = rect.getHeight()
        widthSum = (width1 + width2) / 2
        heightSum = (width1 + height2) / 2

        if abs(pos1[0] - pos2[0]) < widthSum:
            if abs(pos1[1] - pos2[1]) < heightSum:
                if abs(pos1[2] - pos2[2]) < widthSum:
                    return True
        return False
