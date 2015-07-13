__author__ = 'Ming'

class Factory:
    def __init__(self):
        self.object_map = {}

    def regist(self, object_name, createBy):
        self.object_map[object_name] = createBy

    def create(self, object_name, *args, **kwargs):
        return self.object_map[object_name]