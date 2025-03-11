print("Welcome to the Calculator")

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero"
    return round(n1 / n2, 2)

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("Enter the first number: "))
    for i in operations:
        print(i)
    operation = input("Enter the operation you want to perform: ")
    num2 = float(input("Enter the second number: "))
    if operation == "+":
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif operation == "-":
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif operation == "*":
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif operation == "/":
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input")

while True:
    calculator()
    more_calculations = input("Do you want to perform more calculations? Type 'yes' or 'no': ").lower()
    if more_calculations == "no":
        print("Goodbye")
        break
    elif more_calculations != "yes":
        print("Invalid input")
        break
