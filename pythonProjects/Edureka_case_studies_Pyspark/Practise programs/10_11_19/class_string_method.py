class Employee:
    def __init__(self, name, salary):
        print("Initializing variables...")
        self.name = name
        self.salary = salary
    def __str__(self):
        return self.name + " " + str(self.salary)

emp1 = Employee("Shasank", 341631863836136873)
print(emp1)