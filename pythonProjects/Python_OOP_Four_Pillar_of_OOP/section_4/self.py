class Employee:
    def employeeDetails(self):
        self.name = "Mathew"
        print("Name: ", self.name)
        # This is valid only for this method as "self" is not used
        age = 30
        print("Age: ", age)

    def printEmployeeDetails(self):
        print("Instantiating from naother method")
        print("Name:", self.name)
        print("Age: ", age)

employee = Employee()
print(employee.employeeDetails())
print(employee.printEmployeeDetails()) # It will print only name and throw an error while accessing age as it does not have self in it



