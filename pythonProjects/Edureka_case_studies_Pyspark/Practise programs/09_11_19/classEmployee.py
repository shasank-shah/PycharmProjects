class Employee:
    no_of_employees = 0
    def __init__(self, name, salary):
        Employee.no_of_employees += 1
        self.name = name
        self.salary = salary
    def printVal(self):
        print(self.name, self.salary)
obj1 = Employee('Shasank', 10000000)
obj2 = Employee('Vishal', 20000000)
obj3 = obj1
print("No of employees: ", Employee.no_of_employees)
print(obj1.printVal(), obj2.printVal(), obj3.printVal())

