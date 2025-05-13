# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name            # public variable
        self._salary = salary      # protected variable
        self.__ssn = ssn           # private variable

    def get_masked_ssn(self):
        # Show only last 4 digits of SSN — this is safe
        return "***-**-" + self.__ssn[-4:]


employee = Employee("John Doe", 50000, "123-45-6789")  # Creating an instance of Employee 
#print(employee.ssn)         # Raises AttributeError: 'Employee' object has no attribute 'ssn' not handled by the class

# Accessing the public and protected variables

print(employee.name)          # Accessible public variable
print(employee._salary)      # Accessible but should be treated as protected

# Error handling for private variable access
# The private variable __ssn is not accessible outside the class, and trying to access it will raise an AttributeError.
try:
    print(employee.__ssn)      # Raises AttributeError: 'Employee' object has no attribute '__ssn'
except AttributeError as e:
    print("Private variable can not be accessable out of the class" , e)    
                  # Output: 'Employee' object has no attribute '__ssn'
print(f" Name mangling: {employee._Employee__ssn}")  # Not recommended, but works because of name mangling oops principle of encapsulation is breaking , rule broken

 # Accessing the prinvate variable in a recomended way as full info is hidden and only last 4 digits are shown

#  Abstraction	Showing only the essential information, hiding details


print(f"Accessing via get_masked method: {employee.get_masked_ssn()}")  # Output: ***-**-6789