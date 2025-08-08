#Inventory Management

inventory = {
    "Laptop": {"stock": 10, "price": 55000},
    "Mouse": {"stock": 50, "price": 500},
}

# Sell 2 laptops
inventory["Laptop"]["stock"] -= 2

# Update price of Mouse
inventory["Mouse"]["price"] = 450

print(inventory)

#Output:{'Laptop': {'stock': 8, 'price': 55000}, 'Mouse': {'stock': 50, 'price': 450}}