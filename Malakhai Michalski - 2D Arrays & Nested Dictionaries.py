# Malakhai Michalski - 2D Arrays & Nested Dictionaries
# April 30th, 2024

# This will assign names as well as health points for the charecters
charecters = {1: {'name': "Micheal", "health": "Micheal has three health points"},
          2: {'name': "\nAiysha", 'health': "Aiysha has three health points"},
          3: {'name' : "\nHayden", "health" : "Hayden has three health points\n"}}

# This will print the charecters names as well as their health points
print(charecters[1]['name'])
print(charecters[1]['health'])
print(charecters[2]['name'])
print(charecters[2]['health'])
print(charecters[3]['name'])
print(charecters[3]['health'])

# This will create the locations as well as give them a description
location = ("1. The Toxic Tundra is a desolate and eerie wasteland.", "2. The Underground Network is a 24/7 market.", "3. The Citadel is a small city from thousands of years ago.",
            "4. Ruin's Edge is a stoney and dangerous path.")
sorted_location = sorted(location)

# This will print the locations as well as sort them
print("Location")
for item in sorted_location:
    print(item)
    
    
#This will create the weapons,consumables and protection, as well as give them a description
weapons = ("3. Crowbar\n Opens doors as well as damages enemies\nDamange: 25",
           "1. * Machete\n Chops down enemies\n Damage:50", "2. * Energy Sword\n Slices enemies like butter\n Damage: 100")
consumables = ("3. Bandages", "2. Healing Potion", "1. Cursed Bread")
protection = ("2. Jewlery", "1. Bulletproof Vest", "3. Red Hat")

# This will sort the weapons, consumables and protection
sorted_weapons = sorted(weapons)
sorted_consumables = sorted(consumables)
sorted_protection = sorted(protection)

# This will print each charecters available inventory
print("\nMicheal's Inventory:")
for item in sorted_weapons:
    print(item)
    
print("\nAiysha's Inventory:")
for item in sorted_weapons:
    print(item)
    
print("\nHayden's Inventory:")
for item in sorted_weapons:
    print(item)
    
    
    






