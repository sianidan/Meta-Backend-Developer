# Array of desserts
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisu', 'Chocolate Cake']

# For loop
## original for loop with no access to the array index
for item in favorites:
  print('One of my favorite desserts is', item)

## for loop with access to array index; displays index and value of each item in the array
for idx, item in enumerate(favorites):
  print(idx, item)

# While loop; must declare a counter to prevent infinite loop
count = 0

while count < len(favorites):
  print('One of my favorite desserts is', favorites[count])
  count += 1