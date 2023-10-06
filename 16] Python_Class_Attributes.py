class Employee:
    # Class Attribute
    empCount = 0

    # Constructor of class
    def __init__(self, name, salary):
        self.emp_name = name
        self.emp_salary = salary
        Employee.empCount += 1
    
    #  Method of class

    def displayEmployeeInfo(self):
        print("Employee name : ",self.emp_name, " , Employee Salary : ",self.emp_salary)
    
    
    #  Method of class
    
    def displayEmployeeCount(self):
        print("Employee_count",Employee.empCount)

emp1 = Employee( "Pritam" , 7000000 )
emp1.displayEmployeeInfo()
emp1.displayEmployeeCount()

emp2 = Employee( "Pranit" , 5000000 )
emp2.displayEmployeeInfo()
emp2.displayEmployeeCount()

