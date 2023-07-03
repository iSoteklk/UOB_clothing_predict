import csv
import random

clothing_names = ['Shirt', 'Pants', 'Dress',
                  'Jacket', 'Skirt', 'Blouse', 'Jeans', 'T-shirt']
situations = ['Wedding', 'Party', 'Work', 'Casual', 'Formal', 'Outdoor']
colors = ['Red', 'Blue', 'Green', 'Black', 'White', 'Yellow', 'Pink', 'Purple']

records = []
for _ in range(100):
    clothing_name = random.choice(clothing_names)
    situation = random.choice(situations)
    color = random.choice(colors)
    record = {'Clothing name': clothing_name,
              'Situation': situation, 'Color': color}
    records.append(record)

# Export the data to a CSV file
filename = 'clothing_data.csv'
fieldnames = ['Clothing name', 'Situation', 'Color']

with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)

print("Data exported successfully to", filename)
