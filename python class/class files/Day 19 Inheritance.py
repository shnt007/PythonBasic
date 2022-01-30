# inheritance - inherits the parent properties

# inheritance - single, hierarchy, multiple

# shape  area  perimeter
# Triangle - acute angled, right angled, normal
# Quardelateral - square, rhombus, rectangle
# Cirle - ellipse, circle, oval
# Hexagonal, octagonal

#Note
# 1. super() - this function brings all properties of
# parent class
# 2. super() method is define inside the constructor of child class
# 3. if constructor is written inside the child class
# then it doesn't inherit the properties of parent class
# 4. we must define parent class construcuter inside the child class constructor

# python
# class Shape:
#   no_of_sides = 0
#   def __init__(self, no_of_side):
#       self.no_of_sides = no_of_side

# constructor with class name inheritance
# class Triangle(Shape):
#   def __init__(self):
#       Shape.__init__()
#       self.no_of_sides = 5

# constructor with super method
# class Triangle(Shape):
#   def __init__(self):
#       super().__init__()
#       self.no_of_sides = 4

# not defining constructor
# class Triangle(Shape):
#   def get_shape(self):
#       self.no_of_sides = 7

# defining multiple constructor
# constructor overloading - python doesnot support it
# 
# class Area:
#   def __init__(self):
#       self.length
#       self.breadth
#       self.height
#
#   def __init__(self, len, br, hg):
#       self.length = len
#       self.breadth = br
#       self.height = hg
#
#   def __init__(self, len, br):
#       self.length = len
#       self.breadth = br

# example __del__

class Area:
    area = 0
    def __init__(self, area):
        self.area = area

    def areaMethodTest(self):
        print("This is parent class method")

class Triangle(Area):
    length = 0
    breadth = 0
    height = 0
    def __init__(self, l, b, h):
        super().__init__(self)
        self.l = l
        self.b = b
        self.h = h

    def showArea(self):
        self.area = 0.5*self.l*self.h*self.b
        print(self.area)

obj = Triangle(1, 3, 5)
obj.showArea()
obj.areaMethodTest()    


