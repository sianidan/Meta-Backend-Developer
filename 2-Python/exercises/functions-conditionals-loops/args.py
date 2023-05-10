# When declaring a function with parameters, it only allows that particular amount of arguments to be passed 

## a function with 2 specified parameters
def sum1(a, b):
    return a + b

print(sum1(4, 5)) # returns the sum
# print(sum1(4, 5, 6)) returns a TypeError if you pass 3 arguments

# Use *args to allow any number of non-keyword variables to be passed as arguments
def sum2(*args):
    sum = 0
    for x in args:
        # add all values that are passed in as args
        sum += x
    return sum

print(sum2(3, 4, 5))
print(sum2(5, 10, 2, 34))