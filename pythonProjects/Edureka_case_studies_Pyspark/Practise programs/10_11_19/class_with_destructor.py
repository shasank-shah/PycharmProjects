class EmployeeDestructor:
    no_of_emp = 0
    def __init__(self, name, salary):
        print("Initializing variables")
        EmployeeDestructor.no_of_emp += 1
        self.name = name
        self.salary = salary
    def printVar(self):
        print(self.name, self.salary)
'''
    def __del__(self):
        print("Removing: ", self.name, " and his salary: ", self.salary)
        Employee.no_of_emp -= 1
'''