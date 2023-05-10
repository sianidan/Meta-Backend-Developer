# MATH OPERATORS
## Addition 
print(2 + 2)

## Subtraction
print(2 - 2)

## Division; value returned is a float
print(35 / 5)

## Multiplication
print(25 * 4)

# LOGICAL OPERATORS
## AND
a = True
b = True
if a and b:
  print('All true') # prints All true

c = True
d = False
if c and d:
  print('All true') # prints nothing

# OR operator
e = True
f = False
if e or f:
  print('True; one is true and one is false') # prints True

g = False
h = False
if g or h:
  print('All true') # prints nothing

# NOT operator
i = False
j = False
if not(i) or not(j):
  print('All true') # prints All true

k = True
l = True
if not(k) or not(l):
  print('All true') # prints nothing