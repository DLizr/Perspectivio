from src.rendering.object.StaticSceneObject import StaticSceneObject


class StaticCube(StaticSceneObject):

    def __init__(self, centerPosition: list, width, colors: list=None):
        self.__centerPos = centerPosition
        self.__width = width
        vertices = self.genVertices()
        indices = [1, 3, 7, 5, 
                   3, 2, 6, 7, 
                   2, 6, 4, 0, 
                   0, 4, 5, 1, 
                   1, 3, 2, 0, 
                   7, 6, 4, 5]
        if not colors:
            colors = [1.0] * 24
        super().__init__(vertices, indices, colors)
    
    def genVertices(self) -> list:
        vertices = []
        offset = [-self.__width / 2, self.__width / 2]
        for x in offset:
            for y in offset:
                for z in offset:
                    vertices.extend([float(self.__centerPos[0] + x), 
                                     float(self.__centerPos[1] + y), 
                                     float(self.__centerPos[2] + z)])
        return vertices
