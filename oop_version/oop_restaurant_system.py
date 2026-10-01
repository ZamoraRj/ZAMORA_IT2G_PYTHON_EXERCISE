# ============================================================
# PYTHON OOP VERSION: RESTAURANT ORDERING SYSTEM
# ============================================================

class MenuItem:
    """Represents an individual food or drink item on the menu."""
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Menu:
    """Manages the collection of menu items."""
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name.title()] = MenuItem(item_name.title(), price)

    def display(self):
        print("\n" + "=" * 50)
        print("                 BITE & GO ZAMORA")
        print("                  FULL MENU")
        print("=" * 50)

        for name, item in self.items.items():
            print(f"{item.name:<35} ₱{item.price:>8.2f}")

        print("=" * 50)

    def get_item(self, item_name):
        return self.items.get(item_name.title())


class Order:
    """Manages ordered items and quantities."""
    def __init__(self):
        self.ordered_items = {}  # Key: MenuItem object, Value: quantity

    def add_item(self, menu_item, quantity):
        if menu_item in self.ordered_items:
            self.ordered_items[menu_item] += quantity
        else:
            self.ordered_items[menu_item] = quantity

    def calculate_subtotal(self):
        subtotal = 0.0
        for item, qty in self.ordered_items.items():
            subtotal += item.price * qty
        return subtotal

    def is_empty(self):
        return len(self.ordered_items) == 0


class Receipt:
    """Handles receipt calculations and rendering."""
    def __init__(self, order):
        self.order = order

    def calculate_discount(self, subtotal):
        if subtotal >= 1000:
            rate = 0.10
        elif subtotal >= 500:
            rate = 0.05
        else:
            rate = 0.00

        discount = subtotal * rate
        return discount, rate

    def print_receipt(self):
        subtotal = self.order.calculate_subtotal()
        discount, discount_rate = self.calculate_discount(subtotal)
        final_total = subtotal - discount

        print("\n\n")
        print("=" * 65)
        print("                    BITE & GO ZAMORA")
        print("                 CUSTOMER RECEIPT")
        print("=" * 65)

        print(f"{'ITEM':<25}{'QTY':>8}{'PRICE':>14}{'TOTAL':>15}")
        print("-" * 65)

        for item, quantity in self.order.ordered_items.items():
            total_price = item.price * quantity
            print(
                f"{item.name:<25}"
                f"{quantity:>8}"
                f"₱{item.price:>13.2f}"
                f"₱{total_price:>14.2f}"
            )

        print("-" * 65)
        print(f"{'SUBTOTAL':<50}₱{subtotal:>13.2f}")

        if discount_rate > 0:
            print(
                f"{'DISCOUNT (' + str(int(discount_rate * 100)) + '%)':<50}"
                f"-₱{discount:>12.2f}"
            )
        else:
            print(f"{'DISCOUNT':<50}₱{discount:>13.2f}")

        print("=" * 65)
        print(f"{'TOTAL AMOUNT':<50}₱{final_total:>13.2f}")
        print("=" * 65)
        print("              Thank you for ordering!")
        print("                 Please come again!")
        print("=" * 65)


class RestaurantSystem:
    """Coordinates the full ordering flow."""
    def __init__(self):
        self.menu = Menu()
        self.order = Order()
        self.load_default_menu()

    def load_default_menu(self):
        default_items = {
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
        for name, price in default_items.items():
            self.menu.add_item(name, price)

    def prompt_order(self):
        while True:
            item_name = input("\nEnter the menu item: ").strip().title()
            menu_item = self.menu.get_item(item_name)

            if menu_item:
                while True:
                    try:
                        quantity = int(input("Enter quantity: "))
                        if quantity > 0:
                            self.order.add_item(menu_item, quantity)
                            return
                        else:
                            print("Quantity must be greater than 0.")
                    except ValueError:
                        print("Invalid quantity. Please enter a whole number.")
            else:
                print("Sorry, that item is not on the menu.")
                print("Please choose an item from the menu.")

    def run(self):
        self.menu.display()

        while True:
            start = input("\nWould you like to place an order? (yes/no): ").strip().lower()
            if start == "yes":
                break
            elif start == "no":
                print("\nThank you for visiting Jolly Bites!")
                print("Have a great day!")
                return
            else:
                print("Invalid answer. Please enter yes or no.")

        while True:
            self.prompt_order()

            while True:
                another = input("\nWould you like to order another item? (yes/no): ").strip().lower()
                if another in ["yes", "no"]:
                    break
                else:
                    print("Invalid answer. Please enter yes or no.")

            if another == "no":
                break

        receipt = Receipt(self.order)
        receipt.print_receipt()


if __name__ == "__main__":
    app = RestaurantSystem()
    app.run()