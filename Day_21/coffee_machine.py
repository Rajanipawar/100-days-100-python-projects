# Print report
# Check resources sufficient?
# Process coins
# Check transaction is successful?
# Make coffee
print("********** Hello!! Welcome to Coffee Machine..**********")
MENU = {
    'espresso' : {
        "ingredients" : {
            'water' : 50,
            'coffee' : 20,
        },
        "cost" : 2,
    },
    'latte' : {
        "ingredients" : {
            'water' : 60,
            'milk' : 80,
            'coffee' : 30,
        },
        "cost" : 4,
    },
    'cappuccino' : {
        "ingredients" : {
            'water' : 100,
            'milk' : 140,
            'coffee' : 20,
        },
        "cost" : 5,
    }
}

profit = 0
resources = {
    'water' : 200,
    'milk' : 150,
    'coffee' : 180,
}

def is_resources_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are inserted. """
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources.get(item , 0):
            print(f"Sorry there is no enough {item}.")
            return False
        return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    ones = int(input("How many ₹1 coins?: "))
    twos = int(input("How many ₹2 coins?: "))
    fives = int(input("How many ₹5 coins?: "))
    tens = int(input("How many ₹10 coins?: "))
    total = ones * 1 + twos * 2 + fives * 5 + tens * 10
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name,order_ingredients):
    """Deduct required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] = order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")
        

is_on = True

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"water : {resources['water']} ml")
        print(f"milk : {resources['milk']} ml")
        print(f"coffee : {resources['coffee']} g")
        print(f"money : {profit} Rs")
    elif choice in MENU:
        drink = MENU[choice]
        # print(drink)
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink['cost']):
                make_coffee(choice, drink['ingredients'])
    else:
        print("Invalid input.")

