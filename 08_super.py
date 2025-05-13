# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor. 

# Create an instance of Teacher and print the name and subject.

class Person:
    def __init__(self, name):
        self.name = name # constructor is setting name 

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the constructor of the base class (Person)
        self.subject = subject

    def display(self):
        print(f"Teacher's name is: {self.name}")
        print(f"Teacher's subject is: {self.subject}")

details = Teacher("Sir Bilal", "Python")  # Creating an instance of Teacher

details.display()  # Output: Teacher's name is: Sir Bilal, Teacher's subject is: Python