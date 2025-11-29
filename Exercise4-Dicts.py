inventory = {
    "Stylus": 15,
    "Television": 8,
    "Router": 9,
    "Headphones": 25,
    "Iphone": 5
}

inventory["Stylus"] = 15
inventory["Television"] = 12

def low_stock(inv):
    return {k:v for k,v in inv.items() if v < 10}

del inventory["Iphone"]

for product, qty in inventory.items():
    print(product, ":", qty)

print("Low stock products:", low_stock(inventory))
