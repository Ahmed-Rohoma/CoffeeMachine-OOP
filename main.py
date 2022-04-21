from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
while True:
    choice = input("What would you like? "+ menu.get_items())
    if choice == "off":
        break
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        print(choice)
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)





