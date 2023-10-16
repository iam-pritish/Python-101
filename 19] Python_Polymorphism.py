## Fuction Over-riding in Python
## Here we are Writing the Program to find Shape of Object

from math import pi

class Shape():

    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        pass

    def whichShape(self):
        print(self.name)

# For Square

class Square(Shape):
    
    def __init__(self, name, length):
        super().__init__(name)
        self.side_length = length

    def area(self):
        print(self.side_length ** 2 )

    def fact(self):
        print("Square has All sides equal and having each angles at 90 degree.")

# For Circle

class Circle(Shape):

    def __init__(self, name, radius):
        super().__init__(name)                ##  DO NOT FORGET "()" <--- THIS AFTER CALLING 'SUPER' FUNCTION AND THEN PUT '.' IN THERE. 
        self.circle_radius = radius

    def area(self):
        print((self.circle_radius ** 2) * pi)

    def fact(self):
        print("Circle has same Redius through.")    

# Insert the values

sq = Square('Square', 7 )
cr = Circle('Circle', 4 ) 

sq.area()               #-->49

sq.fact()               #-->Square has All sides equal and having each angles at 90 degree.

cr.area()               #--> 50.26548245743669

cr.fact()               #--> Circle has same Redius through.

sq.whichShape()         #--> Square
cr.whichShape()         #--> Circle
