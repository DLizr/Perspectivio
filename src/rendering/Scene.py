from src.rendering.object.DynamicSceneObject import DynamicSceneObject


class Scene:

    def __init__(self):
        self.__objects = set()
        self.__updatableObjects = set()
        self.__dynamicObjects = dict()

    def putObject(self, obj):
        self.__objects.add(obj)

    def putDynamicObject(self, name, obj):
        self.__dynamicObjects[name] = obj

    def putUpdatableObject(self, obj):
        self.__updatableObjects.add(obj)

    def removeDynamicObject(self, name):
        res = self.__dynamicObjects.pop(name)

        if not res:
            raise KeyError("Dynamic Object with key '" + name + "' doesn't exist!")

    def getDynamicObject(self, name) -> DynamicSceneObject:
        try:
            obj = self.__dynamicObjects[name]
        except KeyError:
            raise KeyError("Unable to find Dynamic Object with name '" + name + "'!")
        return obj

    def getDynamicObjects(self):
        return self.__dynamicObjects.values()

    def getUpdatableObjects(self) -> set:
        return self.__updatableObjects.copy()

    def render(self):
        for obj in self.__objects:
            obj.render()
        for obj in self.__dynamicObjects.values():
            obj.render()
        for obj in self.__updatableObjects:
            obj.render()
