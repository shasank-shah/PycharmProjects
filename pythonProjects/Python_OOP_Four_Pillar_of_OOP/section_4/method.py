class Employee:
    def employeeDetails(self):
        self.name = "Ben"

    #Decorators are methods that take another function  and extends their functionality by denoting @ as the starting symbol.
    # It ignores the binding of object and python executes it without any problem
    @staticmethod
    def welcomeMessage():
        print("Welcome to our organization!")

employee = Employee()
employee.employeeDetails()
print(employee.name)
employee.welcomeMessage()