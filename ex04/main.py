import random

print("Welcome to the PyPassword Generator!")
let = int(input("How many letters would you like in your password?\n"))
sym = int(input("How many symbols would you like?\n"))
num = int(input("How many numbers would you like?\n"))

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()_+"
numbers = "0123456789"

def simple_password():
    password = ""
    for i in range(let):
        password += random.choice(letters)
    for i in range(sym):
        password += random.choice(symbols)
    for i in range(num):
        password += random.choice(numbers)
    return password

def strong_password():
    password = []
    for i in range(let):
        password.append(random.choice(letters))
    for i in range(sym):
        password.append(random.choice(symbols))
    for i in range(num):
        password.append(random.choice(numbers))
    random.shuffle(password)
    return "".join(password)

print("Your simple password is: " + simple_password())
print("Your strong password is: " + strong_password())