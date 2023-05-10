# DECLARATION
my_tuple = (1, 'string', 4.5, True, 'string')

# count method
## returns the number of occurrences of a specified value
print(my_tuple.count('string'))

# index method
## returns the index of the first occurrence of a specified item
print(my_tuple.index('string'))
print(my_tuple.index(4.5))

# ITERATION
for x in my_tuple:
    print(x)