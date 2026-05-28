#Daisha Butler
#Create a global variable balance
#This program defines a function 3 functions that simulate transactions in an atm

#initialize
balance = 10000

def deposit():
    global balance
    amount = int(input("How much would you like to deposit? "))
    balance = balance + amount
    print(f"Deposited {amount}")

def withdraw():
    global balance
    amount = int(input("How much would you like to withdraw? "))
    balance = balance - amount
    print(f"Withdrawed {amount}")

def total_balance():
    print(f"Balance = {balance}")

deposit()
withdraw()
total_balance()
