from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menus = Menu()
menuItems = menus.get_items().split("/")  # ['latte', 'espresso', 'cappuccino', ''] or you can the following:
menuItem = [item for item in menuItems]  # ['latte', 'espresso', 'cappuccino', ''] the same as above.

coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

off = False
print(menuItems)

while not off:
    request = input(f"What would you like? ({menus.get_items()} 🍵☕?): ")

    if request in menuItem:
        coffee = menus.find_drink(request)
        cost = coffee.cost

        if coffeeMaker.is_resource_sufficient(coffee) and moneyMachine.make_payment(cost):
            coffeeMaker.make_coffee(coffee)

    elif request == 'off':
        print("Shutting down...")
        off = True

    elif request == 'report':
        coffeeMaker.report()
        moneyMachine.report()

    else:
        print("Invalid input! Please try again...")
