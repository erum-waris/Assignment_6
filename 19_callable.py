
# ### 19. **`callable()` and `__call__()`**

# **Assignment:**  
# Create a class `Multiplier` with an `__init__()` to set a factor. Define a `__call__()` method that multiplies an input by the factor. Test it with `callable()` and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        print( x * self.factor)
    
# Testing the Multiplier class

multiplier = Multiplier(5)   # Creating an instance of Multiplier with a factor of 3
multiplier(24)    # calling object/ instance as callable giving value of x