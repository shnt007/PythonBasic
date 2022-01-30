# Class Object
# syntax

# class <class_name> :
#   block of code

class Area:
    
    def show_area(self):
        print("The area")

obj_area = Area()
obj_area.show_area()
print(obj_area.show_area)
print(obj_area)

def show_area():
    print("This is area")

show_area()

# attributes

# constructor - initialize attributes to instantiate them to object
# two types of constructor
# 1. default constructor
# def __init__(self):
#   
# 2. parameterized constructor
# def __init__(self, length, height):
#   self.length = length
#   self.height = height
# destructor

# Java - Area() same as class name . this
# PHP - __construct() - $this
# Python - __init__()

# area class with constructor
class Area_1:
    # initializing attributes (assigning values)
    height = 0
    breadth = 0
    length = 0
    area = 0
    #default constructor
    def __init__(self):
        self.height
        self.length
        self.breadth
    
    #parameterize constructor
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area_of_triangle(self):
        self.area = 1/2*self.length*self.height
        print(self.area)

new_obj = Area_1(12, 12)
new_obj.area_of_triangle()
obj = Area_1(15, 15)
obj.area_of_triangle()

# function vs method
# parameter vs arguments
# parameter -> variable name used while defining the function
# arguments -> values that are pass in the function through parameter

