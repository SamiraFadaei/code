MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

profit = 0
resources = {
    'water': 300,
    "milk": 200,
    "coffee": 100
}

def is_resource_sufficient(ingredients):
    """Check if there are enough resources to make the drink"""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Get coins from user and calculate total amount"""
    print("Please insert coins.")
    quarters = int(input("  How many quarters?: "))
    dimes = int(input("  How many dimes? : "))
    nickles = int(input("  How many nickles? : "))
    pennies = int(input("  How many pennies? : "))
    
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total

def is_transaction_successful(payment, cost):
    """Check if the payment is enough"""
    if payment < cost:
        print(f"Sorry, that's not enough money. ${payment} refunded.")
        return False
    else:
        change = round(payment - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True

def make_coffee(drink, ingredients):
    """Make the coffee and deduct resources"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink}. Enjoy!")

is_on = True
while is_on:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    
    if choice == "off":
        is_on = False
        print("Machine turned off. Goodbye!")
        
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
        
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid choice. Please choose espresso, latte, or cappuccino.")
