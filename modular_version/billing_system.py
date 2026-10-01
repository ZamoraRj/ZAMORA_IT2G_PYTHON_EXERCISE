# ------------------------------------------------------------
# MODULE: billing_system.py
# Purpose: Handles calculations and printing of customer receipts.
# ------------------------------------------------------------

def calculate_orders(orders, menu):
    subtotal = 0
    for item, quantity in orders.items():
        total_price = menu[item] * quantity
        subtotal += total_price
    return subtotal


def calculate_discount(subtotal):
    if subtotal >= 1000:
        discount_rate = 0.10
    elif subtotal >= 500:
        discount_rate = 0.05
    else:
        discount_rate = 0.00

    discount = subtotal * discount_rate
    return discount, discount_rate


def display_receipt(orders, menu, subtotal, discount, discount_rate):
    final_total = subtotal - discount

    print("\n\n")
    print("=" * 65)
    print("                    BITE & GO ZAMORA")
    print("                 CUSTOMER RECEIPT")
    print("=" * 65)
    print(f"{'ITEM':<25}{'QTY':>8}{'PRICE':>14}{'TOTAL':>15}")
    print("-" * 65)

    for item, quantity in orders.items():
        price = menu[item]
        total_price = price * quantity
        print(
            f"{item:<25}"
            f"{quantity:>8}"
            f"₱{price:>13.2f}"
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