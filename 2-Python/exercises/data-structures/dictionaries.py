# DECLARATION
dict1 = {
    1: 'Integer',
    'Name': 'Siani',
    'Age': 25,
    4.0: 'Float',
    True: 'Boolean'
}
print('Original dictionary:', dict1)

# MANIPULATION
## Access a key's value
print('Age value: ', dict1['Age'])

## Add a new item or update an existing one
dict1['New Key'] = 'New Value'
dict1[1] = 'Updated Value'
print('Updated dictionary:', dict1)

## Delete an item
del dict1['New Key']

# ITERATION 
## keys
for x in dict1:
    print('This is a key:', x)

## keys and values using items method
for key, value in dict1.items():
    print(str(key) + ': ' + str(value))

print('Final updated dictionary: ', dict1)