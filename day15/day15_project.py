

from data import MENU

profit = 0.0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report():
    '''Prints the remaining coffee resources and running profit.'''
    report = (
        f"Water: {resources['water']}ml\n"
        f"Milk: {resources['milk']}ml\n"
        f"Coffee: {resources['coffee']}g\n"
        f"Profit: ${profit:.2f}"
    )
    print(report)


def ask_user():
    while True:
        action = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
        if action in ["espresso", "latte", "cappuccino", "report", "off"]:
            return action
        print("Please enter a valid selection.")

def insert_coins():
    print("Please insert coins.")
    while True:
        try:
            total = int(input("How many quarters?: ")) * 0.25
            total += int(input("How many dimes?: ")) * 0.10
            total += int(input("How many nickels?: ")) * 0.05
            total += int(input("How many pennies?: ")) * 0.01
            return round(total, 2)
        except ValueError:
            user_input = input("Invalid input. Do you want to try again? (y/n): ").lower().strip()
            if user_input not in ["y", "yes"]:
                return None

def validate_resources(product):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    product_water = product.get("ingredients", {}).get("water", 0)
    product_milk = product.get("ingredients", {}).get("milk", 0)
    product_coffee = product.get("ingredients", {}).get("coffee", 0)

    missing = []
    if water < product_water:
        missing.append("water")
    if milk < product_milk:
        missing.append("milk")
    if coffee < product_coffee:
        missing.append("coffee")

    if missing:
        print(f"Sorry, there is not enough: {', '.join(missing)}.")
        return False
    return True

def validate(product, total_payment) -> tuple[bool, float | None]:
    '''Validate selection, resources, and payment. Returns (success, change).'''
    if product is None:
        print("Invalid selection...")
        return False, total_payment

    if total_payment is None:
        print("Transaction cancelled. Refunding payment.")
        return False, None

    if not validate_resources(product):
        return False, total_payment

    product_cost = product["cost"]
    if total_payment < product_cost:
        print("Insufficient payment amount.")
        return False, total_payment

    return True, round(total_payment - product_cost, 2)


def update_resources(product):
    resources["water"] = resources["water"] - product.get("ingredients", {}).get("water", 0)
    resources["milk"] = resources["milk"] - product.get("ingredients", {}).get("milk", 0)
    resources["coffee"] = resources["coffee"] - product.get("ingredients", {}).get("coffee", 0)


def serve_coffee(product, action, change):
    if change and change > 0:
        print(f"\nHere is your change: ${change:.2f}")
    print(f"\nHere is your {action} ☕. Enjoy!")
    update_resources(product)


def main():
    global profit
    while True:
        action = ask_user()
        if action == "off":
            print("Turning off. Goodbye!")
            break
        if action == "report":
            print_report()
            continue

        product = MENU.get(action)
        total_payment = insert_coins()
        result, change = validate(product, total_payment)

        if not result:
            if change is not None and change > 0:
                print(f"Refunding your payment - ${change:.2f}")
            continue

        # Safely extract cost to satisfy static analyzers
        cost = product["cost"] if product is not None else 0.0
        profit += cost
        serve_coffee(product, action, change)

if __name__ == '__main__':
    main()