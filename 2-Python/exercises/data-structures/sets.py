# DECLARATION
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# add method
## adds a specified value to the end of a set
set1.add(6)

# remove method
## removes a specified value from a set; returns an error if the value doesn't exist
set1.remove(3)

# discard method
## removes a specified value from a set if it exists; doesn't return an error if it doesn't
set1.discard(4)

print(set1)
print(set2)

# MATHEMATICAL OPERATIONS
## union method
### joins two sets together, eliminating duplicate values
print(set1.union(set2))
### can also use the OR symbol
set1 | set2

## intersection method
### returns the duplicate values between two sets
print(set1.intersection(set2))
### can also use "&"
set1 & set2

## difference method
### returns the values that are unique to the set it's invoked on compared to another given set
print(set1.difference(set2))
### can also use "-"
set1 - set2

## symmetric difference method
### returns all unique values between two sets
print(set1.symmetric_difference(set2))
### can also use "^"
set1 ^ set2