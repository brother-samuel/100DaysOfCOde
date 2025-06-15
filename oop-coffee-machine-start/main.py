from pickletools import optimize

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
menu = Menu()
#menu_item = MenuItem()

coffee_maker = CoffeeMaker()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order = menu.find_drink(choice)
        #print(order)
        if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)

