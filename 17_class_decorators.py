# ### 17. **Class Decorators**

# **Assignment:**  
# Create a class decorator `add_greeting` that modifies a class to add a `greet()` method returning "Hello from Decorator!". Apply it to a class `Person`.

#class decorator
def add_greeting(cls):

    def greet(self):
        return "Hello from Decorator!"
# Applying the decorator to a class
    cls.greet = greet

    return cls    

# Applying the class decorator to a class   

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Person: {self.name}"
    
    def __iter__(self):
        return iter(self.name)

# Creating an instance of the decorated class

person = Person("Erum Waris")

# Calling the greet method

print(person.greet())

# Calling the __str__ method

person_str = person
print(person_str)



person1 = Person("Waris")

for char in person1:
    print(char)

print(person1)

