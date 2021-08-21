#Check if an employee has achieved his weekly target or not

class Employee:
    name = "Ben"
    designation = "Sales Executive"
    salesMadeThisWeek = 6

    def hasAchievedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print("Sales target has been achieved")
        else:
            print("Sales target not achieved")

employeeOne = Employee()
employeeOne.hasAchievedTarget()