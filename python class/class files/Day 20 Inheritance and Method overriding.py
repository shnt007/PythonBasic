# hierarchy (multi-level inheritance)
# multiple inheritance
# method overriding

# 1. hierarchy (multi-level inheritance)
class Book:
    def book_type(self):
        print("This first edition")

class JavaEE(Book):
    def book_detail(self):
        print("This is enterprise edition")
    
class JavaSE(JavaEE):
    def book_show(self):
        print("This is standard edition")


bookObj = JavaSE()
bookObj.book_show()
bookObj.book_detail()
bookObj.book_type()

class Animal:
    eats = "Eats herb, meat & grass"
    walks = "also they walks"
    breaths = "breath oxygen like human"
    def __init__(self):
        self.eats
        self.walks
        self.breaths

    def animal_basic_character(self):
        print("Animal :" + self.eats + "," + self.walks + " and " + self.breaths)

class Dog(Animal):
    barks = "Barks"
    def __init__(self):
        super().__init__()
        self.barks

    def dog_barks(self):
        print("Dog :" + self.barks + " and carries animal basic characters as well")

class Puppy(Dog):
    sleeps = "Sleeps"
    def __init__(self):
        super().__init__()
        self.sleeps

    def puppy_sleeps(self):
        print("Puppy :" + self.sleeps)
    
objPuppy = Puppy()
objPuppy.animal_basic_character()
print(objPuppy.barks)
objPuppy.dog_barks()
objPuppy.puppy_sleeps()

# multiple inheritance
class Shape:
    def show_shape(self):
        print("Shape of object")

class Area:
    def show_area(self):
        print("Area of object")
        
class Perimeter:
    def show_perimeter(self):
        print("Perimeter of object")

class Circle(Shape, Area, Perimeter):
    def show_details(self):
        print("Circle details")

objCircle = Circle()
objCircle.show_shape()
objCircle.show_area()
objCircle.show_details()


