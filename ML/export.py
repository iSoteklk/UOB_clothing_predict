import csv
import random

# clothing_names = ['Shirt', 'Pants', 'Dress',
#                   'Jacket', 'Skirt', 'Blouse', 'Jeans', 'T-shirt']
situations = ['Wedding', 'Party', 'Work', 'Casual', 'Formal', 'Outdoor']
colors = ['Red', 'Blue', 'Green', 'Black', 'White', 'Yellow', 'Pink', 'Purple']
genders = ['male', 'female', 'unisex']
times = ['night', 'morning', 'evening', 'noon']
categories = ['tousers', 't-shirt', 'shoes', 'jeans', 'waistcoat', 'blouse', 'jacket',
              'dress', 'shirt', 'suit', 'coat', 'shorts', 'sport', 'skirt', 'tops', 'hodie', 'tie']

records = []
for _ in range(10000):
    chosen_category = random.choice(categories)
    color = random.choice(colors)
    clothing_name = chosen_category + '_' + str(random.randint(1, 10000))
    situation = random.choice(situations)
    gender = random.choice(genders)
    time = random.choice(times)
    price = random.randint(1000, 10000)
    record = {'clothing_name': clothing_name+'_'+color,
              'situation': situation, 'color': color, 'gender': gender, 'time': time, 'category': chosen_category, 'price': price}
    records.append(record)

# Export the data to a CSV file
filename = 'clothing_data2.csv'
fieldnames = ['clothing_name', 'situation',
              'color', 'gender', 'time', 'category', 'price']

with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)

print("Data exported successfully to", filename)