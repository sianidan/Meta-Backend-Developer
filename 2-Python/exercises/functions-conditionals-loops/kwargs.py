# Using **kwargs allows you to pass in any number of keyword arguments to a function
def sum1(**kwargs):
    sum = 0

    # get keys and values from a list of the keyword arguments
    for key, value in kwargs.items():
        # add all values that are passed in
        sum += value
    return round(sum, 2)

print(sum1(coffee=3.99, cake=4.55, juice=2.99))