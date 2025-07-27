def calculate_cost(price, quantity):
    return price * quantity

def calculate_discount(cost, discount_rate):
    return cost * discount_rate

def calculate_final_price(cost, discount):
    return cost - discount

def print_final_price(name, price):
    print(f"The final price for {name}: ${price:.2f}")

def process_orders():
    # Discount rate for all items
    discount_rate = 0.05

    # Prices for notebook and pen
    price_notebook, price_pen = 1.99, 0.99

    # Quantities for notebook and pen
    q_notebook, q_pen = 150, 75

    cost_notebook = calculate_cost(price_notebook, q_notebook)
    cost_pen = calculate_cost(price_pen, q_pen)

    # Total price calculation for a notebook with an in-line discount
    if q_notebook > 100:
        discount_notebook = calculate_discount(cost_notebook, discount_rate)
    else:
        discount_notebook = 0
    price_final_notebook = calculate_final_price(cost_notebook, discount_notebook)
    print_final_price('notebook', price_final_notebook)

    # Total price calculation for a pen with an in-line discount
    if q_pen > 100:
        discount_pen = calculate_discount(cost_pen, discount_rate)
    else:
        discount_pen = 0
    price_final_pen = calculate_final_price(cost_pen, discount_pen)
    print_final_price('pen', price_final_pen)

# Call the messy function to process orders
process_orders()
