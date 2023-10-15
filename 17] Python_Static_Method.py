# What is Static methods In Python?

class Car:
    def __init__(self, name,color):
        self.name = name
        self.color = color

    def displayCarDetails(self):
        print("Car Name is",self.name, "and Car Color is",self.color)

    @staticmethod
    def initialMessage():
        print("The Car is Very Nice!!!")

Car.initialMessage()
car1 = Car('XUV 700', 'Red')
car1.displayCarDetails()                        #-->Car name is XUV 700 and Car color is Red

# These are will not WORK
# Car.displayCarDetails()
# print(Car.initialMessage)
# print(Car.displayCarDetails) 
# 
# 
# iNueron Company

class Employee:
    @staticmethod
    def isEmployeeOf():
        print("Employee Class for iNeuron !!!")

Employee.isEmployeeOf()                         #-->Employee Class for iNeuron!!



class Calculation:
    @staticmethod
    def addTwoNums( num1 , num2 ):
        print("Sum of two numbers = ", num1 + num2)

Calculation.addTwoNums(8,5)                         #--> Sum of two numbers = 13
