from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_menu = Menu()
my_money = MoneyMachine()
my_coffee = CoffeeMaker()

while True:
    choice = input(f"What would you like? ({my_menu.get_items()}): ").lower()
    coffee = my_menu.find_drink(choice)
    if choice=="off":
        break
    elif choice=='report':
        my_coffee.report()
        my_money.report()
    elif coffee=='None':
        print(f"No {choice} in this machine")
    else:
        hasCoffee = my_coffee.make_coffee(coffee)
        if hasCoffee:
            if my_money.make_payment(coffee.cost):
                print(f"Here is your {choice} ☕. Enjoy!")

