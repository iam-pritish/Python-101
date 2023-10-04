# how to create a Class
class Employee :
    # Constructor of Class
    # It is mainly used for assignement of instance attribute
     def __init__(self, name, salary):
        # Instance variable or instance Attribute
        self.emp_name = name
        self.emp_salary = salary
    # Method of Class
     def DisplayEmployeeInfo(self):
        print("Emaployee Name:",self.emp_name,",Employee Salary:",self.emp_salary)

emp1 = Employee('Jack',5000)
emp2 = Employee('John',3000)

emp1.DisplayEmployeeInfo()
emp2.DisplayEmployeeInfo()

print(emp1.emp_name)
print(emp2.emp_name)
