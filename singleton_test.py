__author__ = 'Ming'

from Pattern import Singleton

class A:
    def __init__(self, data):
        self.data = data

    def print_data(self):
        print self.data

obj = Singleton.hold(A(10))

t = obj.instance()
t.print_data()
s = obj.instance()
s.print_data()

print t, s

another_obj = Singleton.hold(A(100))
q = another_obj.instance()
q.print_data()
r = another_obj.instance()
r.print_data()

print q, r