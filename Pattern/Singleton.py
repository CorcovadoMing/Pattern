__author__ = 'Ming'

class Singleton:
    _classname = None
    _instance = None

    def __init__(self, classname=None):
        Singleton._classname = classname

    @classmethod
    def instance(self, *args, **kwargs):
        if not Singleton._classname:
            raise ValueError
        elif not Singleton._instance:
            Singleton._instance = Singleton._classname(*args, **kwargs)
        return Singleton._instance