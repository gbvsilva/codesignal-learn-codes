def calculate_total_price(price, quantity):
    return price * quantity

def calculate_discount(total_price, discount_rate):
    return total_price * discount_rate / 100

def calc_price_after_discount(total_price, discount):
    return total_price - discount

def calc_price_with_discount_and_tax(total_price_with_discount, tax_rate):
    return total_price_with_discount * tax_rate / 100

def print_summary(item, single_price, quantity, tax_rate, discount_rate):
    total_price = calculate_total_price(single_price, quantity)
    print(f"Purchasing {quantity} of '{item}'")
    print(f"Original bulk price: ${total_price:.2f}")
    discount = calculate_discount(total_price, discount_rate)
    price_after_discount = calc_price_after_discount(total_price, discount)
    print(f"Price after discount: ${price_after_discount:.2f}")
    price_with_tax = calc_price_with_discount_and_tax(price_after_discount, tax_rate)
    print(f"Total price with tax: ${(price_after_discount) + (price_with_tax):.2f}")

ITEM_NAME = "Premium Coffee Maker"
SINGLE_ITEM_PRICE = 99.99
QUANTITY = 5
TAX_RATE = 7  # Tax rate in percent
DISCOUNT_RATE = 10  # Discount rate in percent

print_summary(ITEM_NAME, SINGLE_ITEM_PRICE, QUANTITY, TAX_RATE, DISCOUNT_RATE)
