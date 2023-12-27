on = True

def add():
    a = float(input("Enter a number"))
    b = float(input("Enter the another number"))
    print(a+b)

def sub():
    a = float(input("Enter a number"))
    b = float(input("Enter the another number"))
    print(a-b)

def mul():
    a = float(input("Enter a number"))
    b = float(input("Enter the another number"))
    print(a*b)

def div():
    a = float(input("Enter a number"))
    b = float(input("Enter the another number"))
    print(a/b)

while on:
    operation = input("Please type +,-,*,/, or q")
    if operation == "+":
        add()
    elif operation == "-":
        sub()
    elif operation == "*":
        mul()
    elif operation == "/":
        div()
    elif operation == "q":
        on = False
    else:
        print("Invalid operation not available")
