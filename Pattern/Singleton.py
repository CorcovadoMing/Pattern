__author__ = 'Ming'

class Singleton:
    def __init__(self):
        pass

    @classmethod
    def hold(cls, ins=None):
        if not ins:
            raise ValueError
        else:
            class _Singleton:
                def __init__(self):
                    self._instance = ins

                def instance(self):
                    return self._instance

            return _Singleton()
