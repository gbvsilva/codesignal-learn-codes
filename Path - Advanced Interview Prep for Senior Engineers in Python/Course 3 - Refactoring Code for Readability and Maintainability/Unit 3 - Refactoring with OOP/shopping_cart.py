class InventoryItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total_price(self):
        return sum(item.price for item in self.items)

# Adding items to the shopping cart
cart = ShoppingCart()
cart.add_item(InventoryItem("Keyboard", 99.99))
cart.add_item(InventoryItem("Mouse", 49.99))
cart.add_item(InventoryItem("Monitor", 149.99))

# Calculating the total price of the cart
print(f"The total price of the shopping cart is: ${cart.calculate_total_price():.2f}")
