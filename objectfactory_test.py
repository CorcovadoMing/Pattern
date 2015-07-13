__author__ = 'Ming'

def test():
    from Pattern import ObjectFactory

    class Line:
        def __init__(self, length):
            self.length = length

        def show_info(self):
            print "The length of the line is ", self.length

    class Circle:
        def __init__(self, radius):
            self.radius = radius

        def show_info(self):
            import math
            print "The area of the circle is ", math.pow(self.radius, 2) * math.pi

    objfac = ObjectFactory.Factory()

    objfac.regist('line', createBy=Line)
    objfac.regist('circle', createBy=Circle)

    myline = objfac.create('line')(10)
    myline.show_info()

    mycircle = objfac.create('circle')(10)
    mycircle.show_info()

