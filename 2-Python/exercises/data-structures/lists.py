# Practice with list manipulation. This covers Declaration, Nested Lists, Adding/Removing list items, Iteration, and Printing Lists

# DECLARING A LIST
## list of integers
list1 = [1, 2, 3, 4, 5] 

## list of strings
list2 = ['A', 'B', 'C', 'D'] 

## list of various data types
list3 = ['Hello', 1, True, 40.22]

# NESTED LISTS
list4 = [1, [2, 3, 4], 5, 6]

# ADDING ITEMS
## insert method
### inserts a given value at a specified index - this will insert the value 6 at index 2
list3.insert(2, 6)

## append method
### adds a given value at end of list
list2.append('E')

## extend method
### adds one or more items to the end of a list
list1.extend([6, 7, 8, 9])

# REMOVING ITEMS
## pop method
### removes an item at a specified index
list1.pop(4)

## del keyword
### removes an item at a specified index
del list2[3]

# ITERATION
## for loop
for x in list3:
    print('Value: ', x)

# PRINTING A LIST
## specific element by index
print(list1[2])

# entire list
print(*list1)
print(*list2)

# entire list in array format; enclosed in [] and separated by a space
print(list3, sep = ' ')