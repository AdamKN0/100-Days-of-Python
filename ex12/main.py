print("Welcome to the Coffee Machine!")

data = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "price": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "price": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "price": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def report():
    for key, value in resources.items():
        print(f"{key}: {value}")

def check_resources(choice):
    for key, value in data[choice]["ingredients"].items():
        if resources[key] < value:
            print(f"Sorry there is not enough {key}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

def make_coffee(choice):
    for key, value in data[choice]["ingredients"].items():
        resources[key] -= value
    resources["money"] += data[choice]["price"]
    print(f"Here is your {choice} ☕️. Enjoy!")

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): or 'off' to turn off the machine or 'report' to see the resources: ").lower().strip()
    if choice == "off":
        break
    elif choice == "report":
        report()
    elif choice in data:
        if check_resources(choice):
            print(f"The price of {choice} is ${data[choice]['price']:.2f}")
            money_received = process_coins()
            if money_received < data[choice]["price"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = money_received - data[choice]["price"]
                if change > 0:
                    print(f"Here is ${change:.2f} in change.")
                make_coffee(choice)
        else:
            continue
    else:
        print("Invalid choice")