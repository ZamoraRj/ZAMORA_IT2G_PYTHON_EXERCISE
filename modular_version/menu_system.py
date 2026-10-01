# ------------------------------------------------------------
# MODULE: menu_system.py
# Purpose: Handles menu items and order processing functions.
# ------------------------------------------------------------

def get_default_menu():
    return {
        "Chickenwings": 99.00,
        "Spaghetti": 60.00,
        "Combo burger": 45.00,
        "Cheesy burger": 55.00,
        "Buff Steak": 75.00,
        "French Fries": 50.00,
        "Mango Pie": 45.00,
        "Chocolate Coke": 50.00,
        "Coke Matcha": 40.00,
        "Pineapple Juice": 45.00
    }


def display_menu(menu):
    print("\n" + "=" * 50)
    print("                 BITE & GO ZAMORA")
    print("                  FULL MENU")
    print("=" * 50)

    for item, price in menu.items():
        print(f"{item:<35} ₱{price:>8.2f}")

    print("=" * 50)


def get_order(menu):
    while True:
        item = input("\nEnter the menu item: ").strip().title()

        if item in menu:
            while True:
                try:
                    quantity = int(input("Enter quantity: "))
                    if quantity > 0:
                        return item, quantity
                    else:
                        print("Quantity must be greater than 0.")
                except ValueError:
                    print("Invalid quantity. Please enter a whole number.")
        else:
            print("Sorry, that item is not on the menu.")
            print("Please choose an item from the menu.")