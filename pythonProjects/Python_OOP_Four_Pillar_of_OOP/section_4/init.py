# To initialize all the attributes before using it in methods.

class Employee:
    def __init__(self, name):
        self.name = name

    def displayEmpoyeeDetails(self):
        print(self.name)

employeeOne = Employee("Mark")
employeeTwo = Employee("Matthew")
employeeOne.displayEmpoyeeDetails()
employeeTwo.displayEmpoyeeDetails()
