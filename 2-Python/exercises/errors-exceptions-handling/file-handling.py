file = open('test.txt', mode = 'r')

data = file.readline()

print(data)
file.close()

with open('test.txt', mode = 'r') as file:
    data2 = file.readline()
    print(data2)

# Creating a file and writing text to it
## \n adds a line break
""" 
with open('newfile.txt', 'w') as file:
    file.write("This is a new file I created.")
    file.writelines(["\nThis is a new line.", "\nThis is another new line."])
"""

# Appending text to the file without overwriting it
with open('newfile.txt', 'a') as file:
    file.writelines(["\nThis is another new line.", "\nThis is another new line."])

# Using Exception Handling
try: 
    with open('sample/newfile.txt', 'a') as file:
        file.writelines("This is a new file.")
except FileNotFoundError as e:
    print("ERROR: ", e)

