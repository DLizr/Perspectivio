class CollisionChecker:

    @staticmethod
    def checkCollisionOfTwoCubes(cube1, cube2):
        """Cube: (centerX, centerY, centerZ, width)"""
        widthSum = (cube1[3] + cube2[3]) / 2

        if abs(cube1[0] - cube2[0]) < widthSum:
            if abs(cube1[1] - cube2[1]) < widthSum:
                if abs(cube1[2] - cube2[2]) < widthSum:
                    return True
        return False   
