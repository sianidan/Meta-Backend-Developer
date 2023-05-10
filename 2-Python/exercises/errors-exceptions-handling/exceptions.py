def divide_by(a, b):
    return a / b

print(divide_by(40, 4))

# If we try to divide by 0, we get a ZeroDivisionError
# print(divide_by(40, 0))

# Handling errors so the user won't see the exception printed out:
## the try statement contains the code you want to execute, and the except statement contains code to execute if an exception occurs
## Get access to the exception information: add the base class Exception and "as e" to except statement
## Get access to the type/class of the exception: e.__class__
try: 
    ans = divide_by(40, 0)
except Exception as e:
    print("Error! Something went wrong: ", e)
    print(e.__class__)

## Give end user more specific information
try: 
    ans = divide_by(40, 0)
except ZeroDivisionError as e:
    print(e, 'we cannot divide by zero')

# Handling more than one exception when you don't know what they are ahead of time
## Chain except statements together
try: 
    ans = divide_by(40, 0)
except ZeroDivisionError as e:
    print(e, 'we cannot divide by zero')
except Exception as e:
    print(e, "Something went wrong")