# 06. Constructor & Destructor Assignment:
# Create a class Logger that prints a message when an object  is created (Constructor) and another message it is destroyed(destructor).


class Logger():

    # Constructor
    def __init__(self):
        print("Logger object has been constructed")
    
    
# Destructor can be invoke directly without creating explicitly a function but it won't print or return anything and this destructor will print output
    def __del__(self):
        print("Logger object has been destructed")


# creating an instance of class

logger_1 = Logger()

# desctructing explicitly invoke destructor

del logger_1
