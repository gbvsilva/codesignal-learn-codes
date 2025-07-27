def calculate_price(quantity, price):
    return quantity * price


def calculate_total_bill(product_quantities, product_prices):
    # Start with a total bill amount of 0
    total_bill = 0
    # Loop through each product in product_quantities dictionary
    for product in product_quantities:
        # Calculate the total price for the product
        total_price = calculate_price(
            product_quantities[product],
            product_prices.get(product, 0))
        # Add the total price of the current product to the total bill
        total_bill += total_price
    # Return the final total bill
    return total_bill

# Product quantities and prices
quantities = {'apple': 2, 'banana': 5, 'cherry': 15}
prices = {'apple': 0.50, 'banana': 0.30, 'cherry': 0.20}

# Compute the total bill for the products
total_bill = calculate_total_bill(quantities, prices)

print(f"Total Bill: ${total_bill:.2f}")
