# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.


class Student:
    def __init__(self, name, marks):
        # Using self keyword assign instance of variable
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Student Marks: {self.marks}")


student_info_1 = Student("Affan" , 450)
Student.display(student_info_1)

student_info_2 = Student("Abdul Raheem" , 550)
Student.display(student_info_2)