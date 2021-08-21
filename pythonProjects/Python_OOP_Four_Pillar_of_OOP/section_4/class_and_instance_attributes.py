class Employee:
    numberOfWorkingHours = 40

employeeOne = Employee()
employeeTwo = Employee()

print(employeeOne.numberOfWorkingHours)
print(employeeTwo.numberOfWorkingHours)

# class attributes would be common to class and we can overwrite the class attribute value
Employee.numberOfWorkingHours = 45 # overwrtiting class attribute value
print(employeeOne.numberOfWorkingHours) # prints 45
print(employeeTwo.numberOfWorkingHours) # prints 45

# Instance attributes is specific to that particular instanciated object
employeeOne.name = "John" # A new attribute is created without having that in class Employee
print(employeeOne.name)

employeeTwo.name = "Mary"
print(employeeTwo.name)

# The flow of attribute is:

#  object instance  ->  class instance  -> Error

# I an attribute is not defined at object instance  -> then it will check in class  -> If its not present in any of them, then it will error out.