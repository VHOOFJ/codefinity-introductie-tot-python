grocery_inventory = {"Milk": ("Dairy", 3.50, 8), "Eggs": ("Dairy", 5.50, 30), "Bread": ("Bakery", 2.99, 15), "Apples": ("Produce", 1.50, 50)}

# Als de prijs van Eggs hoger is dan 5, verlaag dan de prijs met 1
eggs = grocery_inventory.get("Eggs")
if (eggs and eggs[1] > 5):
    print("Eggs are too expensive, reducing the price by $1.")
    eggs_list = list(eggs)
    eggs_list[1] -= 1
    grocery_inventory.update({"Eggs": tuple(eggs_list)})

# Voeg Tomatoes toe aan en print de inventaris af
grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print(f"Inventory after adding Tomatoes: {grocery_inventory}")

# Als de voorraad van Milk kleiner is dan 10, verhoog dan de voorraad met 20
milk = grocery_inventory.get("Milk")
if (milk and milk[2] < 10):
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    milk_list = list(milk)
    milk_list[2] += 20
    grocery_inventory.update({"Milk": tuple(milk_list)})
else:
    print("Milk has sufficient stock.")

# Verwijder Apples als de prijs hoger is dan 2
apples = grocery_inventory.get("Apples")
if (apples and apples[1] > 2):
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

print(f"Updated inventory: {grocery_inventory}")