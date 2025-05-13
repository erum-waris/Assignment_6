# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
    def __init__(self, C):
        self.C = C

    @staticmethod
    def celsius_to_fahrenheit(self, C):
            self.celsius_to_fahrenheit = C
        # Formula for conversion
            return ((C * 9/5) + 32)
       

    def display(self):
            print(f"Fahrenheit of {self.C} Celcius is = {self.celsius_to_fahrenheit}  ")

C = 12
converter = TemperatureConverter(C)
converter.display()