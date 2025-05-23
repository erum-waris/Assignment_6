
# ### 15. **Method Resolution Order (MRO) and Diamond Inheritance**

# **Assignment:**  
# Create four classes:

# -   `A` with a method `show()`,
    
# -   `B` and `C` that inherit from `A` and override `show()`,
    
# -   `D` that inherits from both `B` and `C`.
    

# Create an object of `D` and call `show()` to observe MRO.

 
# polymorphism is implementing as one method is being behaving differently 

class A:
    def show(self):
        print("A is a parent")

class B(A):  #inheritance
    def show(self):  #method over riding
        print("B is a first child")

class C(A):   #inheritance
    def show(self):     #method over riding
        print("C is a second child")

class D(B, C):   # MRO works in order left to right where it will find excecution it will work and execute
    #  def show(self):     #method over riding
    #     print("D is a second child")    # if there will not be any block of code then B will excecute 
    pass  # now B will excecute B is a first child 

d = D() 
d.show()  
print(D.mro())  # class Order finding
print("The MRO for class D can be visualized as a linear sequence: D → B → C → A → object")