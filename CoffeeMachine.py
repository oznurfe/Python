MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


#Get the coffee type
choice = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
coffee = MENU[choice]


#Get the total money
total = 0
print("Please insert coins.")
quarter = int(input("How many quarters?"))
dimes = int(input("How many dimes?"))
nickles = int(input("How many nickles?"))
pennies = int(input("How many pennies?"))


total = quarter * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

#Check if the inserted money is enough.
if total < coffee["cost"]:
    print("Sorry that's not enough money. Money refunded.")
else:
    total -= coffee["cost"]
    print(f"Here is ${total} in change.\nHere is your {choice}☕. Enjoy!")
total = 0

