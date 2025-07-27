# Begin with generic non-descriptive function and variable names
def calculate_cost(quantity, price):
    return quantity * price

def total_cost(name, cost):
    print(f"The total cost for {name} is: ${cost:.2f}")

# Variables for pencil unit prices
pencil1_price = 0.25
pencil2_price = 0.50

# Variables for pencil quantities
pencil1_quantity = 100
pencil2_quantity = 200

# Calculating and printing total costs
pencil1_cost = calculate_cost(pencil1_quantity, pencil1_price)
pencil2_cost = calculate_cost(pencil2_quantity, pencil2_price)

total_cost("pencil1", pencil1_cost)
total_cost("pencil2", pencil2_cost)
