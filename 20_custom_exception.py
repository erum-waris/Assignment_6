# ### 20. **Creating a Custom Exception**

# **Assignment:**  
# Create a custom exception `InvalidAgeError`. Write a function `check_age(age)` that raises this exception if `age < 18`. Handle it with `try...except`.

class InvalidAgeError(Exception):
    pass

#checking age
def check_age(age):
    if age <= 18 or age >= 100:
        raise InvalidAgeError("Age must be 18 or under 100.")
    else:
        print("Access granted.")

# Testing the custom exception

try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")
except ValueError:
    print("Please enter a valid number for age.")

# The code defines a custom exception class `InvalidAgeError` that inherits from the built-in `Exception` class.

