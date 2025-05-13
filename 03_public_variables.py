# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    # Public variable
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is Starting")

# object creating 

my_car = Car("Toyota")

#Accessing Public Variable
print(f"Car Brand is: {my_car.brand}")

# Public method calling

my_car.start()