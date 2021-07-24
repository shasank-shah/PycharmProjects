class Employee:
    no_of_employees = 0
    def __init__(self, name, salary):
        Employee.no_of_employees += 1
        self.name = name
        self.salary = salary
    def printVal(self):
        print(self.name, self.salary)
    @classmethod
    def print_no_of_emp(cls):
        print(cls.no_of_employees)

print(Employee.print_no_of_emp()) # No need to create object.
