# ### 16. **Function Decorators**

# **Assignment:**  
# Write a decorator function `log_function_call` that prints "Function is being called" before a function executes. Apply it to a function `say_hello()`.

def log_function_call(func):
    def wrapper_function():
        print(f"Function is being called")
        return func()
    return wrapper_function

@log_function_call
def say_hello():
    print(f"Hello Hello How are you??")

say_hello()