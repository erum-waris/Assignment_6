# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # Instance method to make the dog bark
    def bark(self):
            print(f"{self.name} says Bow Bow! It is a breed of {self.breed}.")


# creating an instance of Dog class
dog_1 = Dog("Tomy", "German Shepherd")
# calling the instance method bark
dog_1.bark() 