# 05. Static Methods and Static variables Assignment:

# Create a class Mathutils with a static method add(a,b) that returns the sum. No class or instance variable should be used.

class Mathutils:
    
    @staticmethod

    def add(a, b):
        return a + b

Result = Mathutils.add(4,4)

print(f" Sum is : {Result}")