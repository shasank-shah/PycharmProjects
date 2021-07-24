class Employee:
    no_of_emps = 0
    def __init__(self, name, salary):
        print("Initializing variables")
        self.name = name
        self.salary = salary
    def printVal(self):
        print(self.name, self.salary)
    @classmethod
    def emp_using_class_method(cls, salary, name):
        return cls(name, salary)
    @classmethod
    def print_no_of_emps(cls):
        print(cls.no_of_emps)

emp1 = Employee("Shasank", 90000000000)
emp2 = Employee.emp_using_class_method(8000000000000, "Vishal")
print(emp1.printVal())
print(emp2.name, emp2.salary)