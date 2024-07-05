from coffee_menu import MENU, resources


def checkResourcesAvailability(coffee, resource):
    ingredients = MENU[coffee]['ingredients']
    for item in ingredients:
        if resource[item] < ingredients[item]:
            print(f"Sorry, there is not enough {item}...")
            return False
    return True


def checkCoinsAvailability(coffee, coins):
    if coins < MENU[coffee]['cost']:
        print("Sorry that's not enough money... Money refunded!")
        return False
    return True


def makeCoffee(coffee, resource):
    ingredients = MENU[coffee]['ingredients']
    for item in ingredients:
        resource[item] -= ingredients[item]
    return resource, f"\nHere is your {coffee} ☕. Enjoy!"


def offerChange(coffee, coins):
    cost = MENU[coffee]['cost']
    if coins > cost:
        change = round(coins - cost, 2)
        return change, f"\nHere is ${change} in change."


def printReport(resource, coins):
    for item in resource:
        print(f"{item}: {resource[item]}")
    print(f"Money: ${coins}")


penny = 0.01
nickel = 0.05
dime = 0.10
quarter = 0.25

money = 0.0

off = False

while not off:
    request = input("What would you like? (espresso/latte/cappuccino) 🍵☕: ")

    if request in MENU:
        if checkResourcesAvailability(request, resources):
            penny_amount = int(input("How many pennies? "))
            nickel_amount = int(input("How many nickels? "))
            dime_amount = int(input("How many dimes? "))
            quarter_amount = int(input("How many quarters? "))

            total = penny * penny_amount + nickel * nickel_amount + dime * dime_amount + quarter * quarter_amount

            if checkCoinsAvailability(request, total):
                resources, response1 = makeCoffee(request, resources)
                newMoney, response2 = offerChange(request, total)

                print(response1, response2, "\n")
                print(f"Report after purchasing {request}:")
                printReport(resources, newMoney)

    elif request == "report":
        printReport(resources, money)

    elif request == "off":
        off = True
        print("Shutting down...")
        # break
    else:
        print("Invalid input. Please try again...")
