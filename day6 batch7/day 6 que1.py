# Python program to create Bank Account class 
# with two method a deposit() and a withdraw() method
class Bank_Account: 
    def __init__(self):
        self.balance=0
        print("Welcome to the Deposit & Withdrawal Machine","\n") 
        self.ownerName=input("Please enter your name!: ") 
        print("We Are Happy to Have You Here",self.ownerName,"\n")
    def deposit(self):
        
        amount=float(input("Enter the amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount,"\n") 
        print("\n Net Available Balance=",self.balance,"\n")
    def withdraw(self): 
        amount = float(input("Enter the amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount,"\n") 
        else: 
            print("\n Insufficient balance, Try a smaller amount.\n") 
        print("\n Net Available Balance=",self.balance,"\n")               
# Driver code 
   
# creating an object of class 
print("Welcome to OOPython Bank!\n What may I help you with today?\n\n")
User = Bank_Account()
while True: 
    Operations=input("Press D for Deposit, W for Withdraw or E to Exit: ")

    if Operations.upper()!="D" and Operations.upper()!="W" and Operations.upper()!="E":
        print("Invalid input, Try again...\n")
        continue
    if Operations.upper()=="E":
        print("Thank you for choosing OOPython Bank, Have a Great day!")
        break
    if Operations.upper()=="D":
        User.deposit()
        continue
    elif Operations.upper()=="W": 
        User.withdraw()
        continue

# Calling functions with that class object 

'''
Output:
