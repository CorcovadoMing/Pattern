__author__ = 'Ming'

from Pattern import Singleton

class A:
    def __init__(self, data):
        self.data = data

    def print_data(self):
        print self.data

obj = Singleton(A).instance(10)
obj.print_data()

another_obj = Singleton.instance()
another_obj.print_data()

print obj, another_obj