# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Department:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Department: {self.name}")


class Employee:
    def __init__(self, name, department):  #--> agregation : Aggregation ek type ka relationship hota hai OOP mein jahan ek class ke andar doosri class ka object hota hai, lekin dono ka independent existence hota hai.
        self.name = name
        self.department = department
        self.department.display()
        print(f"Employee: {self.name}")

# instance of department 
department = Department("HR")
# instance of employee
employee = Employee("Adil", department)
employee.department.display()