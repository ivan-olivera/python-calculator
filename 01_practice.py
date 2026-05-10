def add(num1, num2):
    return num1 + num2
def substraction(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def division(num1, num2):
    return num1 / num2
while True:
    num1 = float(input("Insert the first number: "))
    num2 = float(input("Insert the second number: "))
    option = str(input("What type of operation you want to do?\n|Add|Substraction|Multiply|Division|Quit| ")).lower()
    if option == "quit":
            break
    elif option == "add":
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
    elif option == "substraction":
            result = substraction(num1, num2)
            print(f"{num1} - {num2} = {result}")
    elif option == "multiply":
            result = multiply(num1, num2)
            print(f"{num1} x {num2} = {result}")
    elif option == "division":
            result = division(num1, num2)
            print(f"{num1} / {num2} = {result}")
    else: 
            print("Invalid operation")


    



