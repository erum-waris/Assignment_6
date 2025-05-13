# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def start(self):
       print("Engine started")
    

class Car:
    def __init__(self, engine):
        self.engine = engine    # Composition:"Composition mein parent class khud hi child object banata hai, aur agar parent object delete ho jaye to child object bhi khatam ho jata hai."


    def start_car(self):
        return (self.engine.start())  # Accesing Engine's method via Car class 

# instance of an Engine class 

engine = Engine()

# instance of a Car class
car = Car(engine)
car.start_car()   # Output: Engine started


