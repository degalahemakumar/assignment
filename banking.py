import sys
class customer:
    bankname="SBI"
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("the balance after the deposit is :",self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient amount, please withdraw with in the balance amount")    
            sys.exit()
        self.balance=self.balance-amount
        print("the balance after the withdraw is ",self.balance)
    def display(self):
        print("net avaliable balance",self.balance)    

print("welcome to ",customer.bankname)
name=input("Enter your name : ")
c=customer(name)
while True:
    print("d-deposit \n w- withdraw \n e- exit")
    option =input(" choose your option ")
    if option=="d":
        amount=int(input("enter the amount to deposit : "))#1000
        c.deposit(amount)
    elif option=="w":
        amount=int(input(" enter the withdraw amount :"))
        c.withdraw(amount)   
    elif option=="n":
        amount=int(input("enter the net amount available:"))
        c.net(amount)
    elif option=="e":
        print("thank you for banking with us ")
        sys.exit()
    else:
        print("invaild option, please select correct option ")