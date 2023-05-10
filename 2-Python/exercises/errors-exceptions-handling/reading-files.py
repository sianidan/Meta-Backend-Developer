# read(): returns the entire contents of the file as a string 
## pass in integer to return a specified number of characters
with open('sample.txt', 'r') as file:
    print(file.read())

with open('sample.txt', 'r') as file:
    print(file.read(44))

# readline(): returns a single line as a string
## pass in integer to read a specified number of characters on a line
with open('sample.txt', 'r') as file:
    print(file.readline())

with open('sample.txt', 'r') as file:
    print(file.readline(10))

# readlines(): reads the entire contents of the file and returns it in an ordered list
with open('sample.txt', 'r') as file:
    print(file.readlines())

## because it's a list, it can be assigned to a variable
with open('sample.txt', 'r') as file:
    data = file.readlines()
    
    for x in data:
        print(x)

# *NOTE* the with open() as file function returns a list by default, so the following code does the same as above:
with open('sample.txt', 'r') as file:
    for x in file:
        print(x)