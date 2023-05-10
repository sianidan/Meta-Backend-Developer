# Handling errors so the user won't see the exception printed out:
## the try statement contains the code you want to execute, and the except statement contains code to execute if an exception occurs
""" 
    - Get access to the exception information: add the base class Exception and "as e" to except statement
    - Get access to the type/class of the exception: e.__class__
    - Give end user more information by using the exception class in the except statement
    - Chain except statements together to handle more than one exception when you don't know what they are ahead of time
"""

# INDEX ERROR
items = [1,2,3,4,5]
try:
    item = items[6]
    print(item)
except IndexError:
    print("The index does not exist in the list.")

# ZERO DIVISION ERROR
def divide_by(a, b):
    try: 
        return a / b
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print(e, "Something went wrong!")

ans = divide_by(20, 0)
print(ans)

# FILE NOT FOUND ERROR
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except Exception as e:
    print(e.__class__)
    print("The file could not be found")
