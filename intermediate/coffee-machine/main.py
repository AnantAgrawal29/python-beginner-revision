coffee = [
     {
        'coffee': 'espresso',
        'resources': {
            'Water': 50,
            'Milk': 0,
            'Coffee': 18, 
            'Money': 1.5 
        }
    },
    {
        'coffee': 'latte',
        'resources': {
            'Water': 200, 
            'Milk': 150, 
            'Coffee': 24, 
            'Money': 2.5
        }
    },
    {
        'coffee': 'cappuccino',
        'resources': {
            'Water': 250, 
            'Milk': 100, 
            'Coffee': 24, 
            'Money': 3.0
        }
    }
]

coins = {
    'Penny' : 0.01,
    'Dime': 0.10,
    'Nickel': 0.05,
    'Quarter': 0.25
}

resources = {
    'Water': 300, 
    'Milk': 200, 
    'Coffee': 100, 
    'Money': 0  
}

def report():
    for items in resources:
        if items == 'Water' or items == 'Milk':
            print(f"{items} : {resources[items]}ml")
        elif items == 'Coffee':
            print(f"{items} : {resources[items]}g")
        else:
            print(f"{items} : ${resources[items]}")

def process_coins():
    money = 0.0
    print("Please insert coins.")
    for coin in coins:
        coin_entered = float(input(f"How many {coin}?: "))
        money += coin_entered*coins[coin]
    return money

def check_resources(bought_coffee):
    for items in resources:
        if bought_coffee[items] > resources[items] and items != 'Money':
            print(f"Sorry there is not enough {items.lower()}")
            return False
    return True

def checkMoney(bought_coffee, money):
    if bought_coffee['Money'] <= money:
        if money > bought_coffee['Money']:
            print(f"Here is ${round(money - bought_coffee['Money'],2)} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def updateResource(coffee_resources,money):
    if checkMoney(coffee_resources, money):
        new_resources = resources
        for items in new_resources:
            if items != 'Money':
                new_resources[items] -= coffee_resources[items]
        new_resources['Money'] += coffee_resources['Money']
        return new_resources
    return False

def make_coffee(coffee_bought):
    coffee_resources = {}
    for drink in coffee:
        if drink['coffee']==coffee_bought:
            coffee_resources = drink['resources']
            break
    if check_resources(coffee_resources):
        money = process_coins()
        return updateResource(coffee_resources,money)
    return False

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice=="off":
        break
    elif choice=='report':
        report()
    elif choice!='espresso' and  choice!='latte' and choice!='cappuccino':
        print(f"No {choice} in this machine")
    else:
        hasCoffee = make_coffee(choice)
        if hasCoffee:
            resources = hasCoffee
            print(f"Here is your {choice} ☕. Enjoy!")