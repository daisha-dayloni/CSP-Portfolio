#Daisha Butler
#Calculator Simple Math
#Create a program that prompts users to enter two numbers, an operator, and prints the result of the operation

def main():
    #Welcome to the user
    print("Welcome to the Simple Claculator!")
    #Collect your input
    num1 =  int(input("Enter a number:" ))
    num2 = int(input("Enter another number:" ))
    operator=input("Enter an operation symbol")
    #perform the operation
    if operator == "+":
        print( calc_sum(num1,num2) )
    if operator == "-":
        print( calc_sub(num1,num2) )
    if operator == "*":
        print( calc_multi(num1,num2) )
    if operator == "/":
        print( calc_div(num1,num2) )

def calc_sum(x,y):
    total = x + y
    return total
def calc_sub(x,y):
    return x-y
def calc_multi(x,y):
    return x*y
def calc_div(x,y):
    return x/y

print (calc_sum(23,89))
main()
