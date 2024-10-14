#Example of a ZERODEVISIONERROR:
try:
    result = 10/0
    print(result)
except ZeroDivisionError:
    print("Sorry a number cannot be divided by zero!")

# result = 10/0
# print(result)

#Typeerror
try:
    result = "10" + 5
except TypeError:
    print("Cannot add a string with an interger")


#File not found error
try:
    with open('acc.py', "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file you are trying to look for does not exist:")
    