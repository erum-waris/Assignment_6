
# ### 18. **Property Decorators: `@property`, `@setter`, and `@deleter`**

# **Assignment:**  
# Create a class `Product` with a private attribute `_price`. Use `@property` to get the price, `@price.setter` to update it, and `@price.deleter` to delete it.

class Product:
    def __init__(self,price,productName):
        self.__price = price
        self.productName = productName
    #getter to get private attribute value
    @property
    def price(self):
        return self.__price
    
   #setter to set private attribute value
    @price.setter
    def price(self,value):
        if value > 0:
            self.__price = value
        
        else:
            print("Please enter a value greater than 0")

    # deleter to delete price attribute
    @price.deleter
    def price(self):
        print(f"Deleting the price of {self.productName}")
        print("Deleted Successfully")
        del self.__price

# instantiating a product

product_1 = Product(4000,"Head Phone")

# getting price using @property
print(product_1.price)

# setting price @price.setter
product_1.price = 30202
print(product_1.price )

# delete or destroy object  using @price.deleter (Destructor del has been called)
del product_1.price


