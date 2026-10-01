# ------------------------------------------------------------
# MAIN PROGRAM: main.py
# Purpose: Imports custom modules to execute the ordering system.
# ------------------------------------------------------------

from menu_system import get_default_menu, display_menu, get_order
from billing_system import calculate_orders, calculate_discount, display_receipt


def main():
    menu = get_default_menu()
    orders = {}

    display_menu(menu)

    while True:
        start_order = input("\nWould you like to place an order? (yes/no): ").strip().lower()

        if start_order == "yes":
            break
        elif start_order == "no":
            print("\nThank you for visiting Jolly Bites!")
            print("Have a great day!")
            return
        else:
            print("Invalid answer. Please enter yes or no.")

    while True:
        item, quantity = get_order(menu)

        if item in orders:
            orders[item] += quantity
        else:
            orders[item] = quantity

        while True:
            another_order = input("\nWould you like to order another item? (yes/no): ").strip().lower()

            if another_order in ["yes", "no"]:
                break
            else:
                print("Invalid answer. Please enter yes or no.")

        if another_order == "no":
            break

    subtotal = calculate_orders(orders, menu)
    discount, discount_rate = calculate_discount(subtotal)
    display_receipt(orders, menu, subtotal, discount, discount_rate)


if __name__ == "__main__":
    main()