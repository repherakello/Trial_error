
add = lambda x, y: x + y 
result = add(30,6)
print(result)

#keyword arguments

def user_info(name , age = None):
    print(f"Name: {name}")
    if age:
        print(f"age: {age}")

user_info(name = "Bob", age =30)

#default argument
def greet(name="world"):
    print("hello", name)
greet("repher")

#return values
"""are values that a function send back to the caller after execution.
Python funtions can return multple vlues as a tuple or tother iterable types"""

def square(number):
   print(number * number)
   
square(4)

#variable scope and functions
# local scope and global scope
"""variables defined within a function is a local function while 
one defined out side is a glaobal func and are accesed everywhere"""
#global

count = 0
def increment_global():
    global count
    count += 1
increment_global()
print(count)

#nested function
def outer_function():
    x = 10

    def inner_function():
        nonlocal x
        x += 5

    inner_function()
    print("Modified value of x from inner function:", x)
outer_function()



#work 1: writing a function which greet the user and returns the name

def called(name):
    print("Hello!How you doing",name)

called("Repher?")

#Work 2: function which calculate the area of a rectangle.

def area_rectangle(length,width):
    area = length * width
    return area

print(area_rectangle(3,6))

def check_odd_even():
    number =eval(input("enter the number:"))
    if number % 2 == 0:
        print("The number is even:",number)
    elif number %2 != 0:
        print("The number is an odd number", number)
    else:
        print("Wrong input!")
check_odd_even()