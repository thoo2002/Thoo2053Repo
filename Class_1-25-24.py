#Inputs/Classes
#Have to cast to work
# num = int(input("enter a number: "))
# print(num)
# num+=10
# print(num)
#try accept except/catch clause
# try:
#     num = int(input("Enter a number: "))
#     num += 10
# except:
#     print("You did not input a number")
# print("continue")
#Look at input solutions for examples
with open("movies.txt") as file:
    for line in file:
        line = line.strip()
        print(line)
with open("heights.txt") as file:
    for line in file:
        line = line.strip()
        tokens = line.split()
        print(tokens)
#classes
# class Bankaccount:
#     def __init__(self, account_number, balance=0.0):
#         self.account_number=account_number
#         self.balance=balance
#     def __str__(self):
#         return self.account_number + ' has the balance ' + str(self.balance)
#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.balance -= amount

#     def get_balance(self):
#         return self.balance
from bank_account import BankAccount
account1=BankAccount('1234567')
account2=BankAccount('7654321', 150.00)
print(account1)
print(account2)
account1.deposit(1000.00)
account2.withdraw(50.00)
