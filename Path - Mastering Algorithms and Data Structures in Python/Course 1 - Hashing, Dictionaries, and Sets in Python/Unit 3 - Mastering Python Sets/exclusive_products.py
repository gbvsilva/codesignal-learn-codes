def exclusive_products(inventory1, inventory2):
    # implement this
    inventory1 = set(item.upper() for item in inventory1)
    inventory2 = set(item.upper() for item in inventory2)
    return list(inventory1 - inventory2), list(inventory2 - inventory1)

inventory1 = ["Shirt", "Jeans", "Hat"]
inventory2 = ["jeans", "Belt", "Boots"]
print(exclusive_products(inventory1, inventory2))
# Expected output: (['HAT', 'SHIRT'], ['BELT', 'BOOTS'])

inventory1 = ["T-Shirt", "hoodie", "Backpack"]
inventory2 = ["Backpack", "Hoodie", "t-shirt"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], [])

inventory1 = []
inventory2 = ["Dress", "Skirt", "Coat"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], ['COAT', 'DRESS', 'SKIRT'])
