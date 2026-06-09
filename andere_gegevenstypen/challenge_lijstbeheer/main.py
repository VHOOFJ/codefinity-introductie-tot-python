# Lijsten initialiseren
meat = ["Ham", 3.99, 50, "sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]

# Hoofdlijst aanmaken
deli_dept = [meat, cheese, condiment]
print(f"Initial Deli List: {deli_dept}")

# Voorraad aanvullen
if (meat[0] == "Ham" and meat[2] < 100):
    meat[2] = 100
print(f"Updated Deli List: {deli_dept}")

# Seizoensvlees toevoegen
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)
print(f"Updated Deli List: {deli_dept}")

# Saus verwijderen
deli_dept.remove(condiment)
print(f"Updated Deli List: {deli_dept}")

#Lijst sorteren
deli_dept.sort()
print(f"Updated Deli List: {deli_dept}")