# Inheritance In Python

#  Base Class AKA Parent Class

class Person:
    def __init__ (self, name):
        self.name = name

    def display_name(self):
        print(self.name)

    # By default we can say that particular Person is Un-employed

    def isEmployed(self):
        print(self.name, "is Un-employed !!!")


# Now , Derived Class/Child Class
class Employee(Person):
    
    def isEmployed(self):
        print(self.name, "is Employed !!!")
        
emp = Person("Shashank")                
emp.display_name()                  #---> Shashank
emp.isEmployed()                    #---> Shashank is Un-employed

emp = Employee("Rosse")
emp.display_name()                  #---> Rosse
emp.isEmployed()                    #---> Rosse is Employed

## How to initilize Constructor of Base Class
## Base class aka Parent Class

class Person:
    def __init__(self, name):
        self.name = name

    def displayName(self):
        print(self.name)


    ## By Default we can say that perticilar person is Un-employed         
    
    def isEnmeployed(self):
        print(self.name,"is Un-Employed..!!")
## Derive class aka child class

class Employee(Person):
    def __init__(self, emp_name, emp_ID, Salary, Designation):
        
        self.emp_ID  = emp_ID
        self.Salary = Salary
        self.Designation = Designation

        
        ## Calling Constructor of Base Class
        #  Person.__init__(self, emp_name)

        super().__init__(emp_name)

        def isEmployee(self):
            print(self.name,"is Employed..!!")

        def employee_Details(self):
            print("Employee ID is",self.emp_ID,
                    "Employee Salary is",self.Salary,
                    "And Employee Designation is",self.Designation)

emp1 = Employee('Jason',8898,120000,'Data Analyst')
emp1.displayName()
print(emp1.name)
emp1.employee_Details()
