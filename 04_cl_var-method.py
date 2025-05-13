# 4. Class Variables & Class Methods

# Create a class Bank with a class variable bank_name . Add a class method change_bank_name(cls, name)that allows changing the bank_name. Show that it affects all instances.

class Bank:
    bank_name = "MCB"
    def __init__(self, account_holder):
    
        self.account_holder = account_holder
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name   # updating bank name

    def display(self):
        print(f"Bank Name is: {self.bank_name} , Account Holder Name is : {self.account_holder} ")


bank_info = Bank("Erum")

bank_info.display()

#updating Bank name

Bank.change_bank_name("HBL")

bank_info.display()


