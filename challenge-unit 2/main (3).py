class BankAccount:
  def__init__(self, account__number, account__holder__name, initial__balance = 0.0)
  self.__account_number = account__number
  self.__account_holder__name = account__holder__name
  self.__account_balance = initial__balance

def deposit(self, amount):
  if amount > 0:
    self.__account__balance += amount
    print(end="\n")
    print("Desposit a, 1{}. New balance:a, 1{}".format(amount,self.__account__balance))
print(end="\n")
print("Invalid deposit amount. Please deposit a positive amount.")

def withdraw(self, amount):
  if amount > 0 and amount <= self.__account__balance:
self.__account__balance -= amount 
  print(end="\n")
  print("Withdraw a, 1{}.New balance:a, 1{}. New balance:a, 1{}". format(amount,self.__account_balance))
 else:
  print("Invalid withdrawl amount 

def display_balance(self):
  print(end="\n")
  print("Account balance for {} (Account#{}):a, 1{}".format(self.__account__holder__name,self.__account__number,self.__account__balance))

#Create an instance of the BankAccount class
class account=BankAccount(account__number="123456789",
                         account__holder__name="Asma",
                         initial__balance=5000.0)

#Test desposit and withdrawl functionality
d=int(input("Enter the amount to desposit:"))
print(end="\n")
w=int(input("Enter the amount to withdraw:"))
account.display__balance()
account.desposit(d)
account.withdraw(w)
account.display__balance()

  
    
        
        
        
                                                                  
        


