# iterating over list
fruits = ["mangoe","pawpaw","guava"]

for fruit in fruits:
    print(fruit)

#iterating over tuples
#tuples are similar to list but are immutable.

colors = ("red","green","purple","blue")

for color in colors:
    print(color)

#iterating over Ranges
for number in range(6):
    print(number)


#coding with mosh examples!

successful = True
for number in range(1,4):
    print("sending a message",number, (number)* ".")
    if successful:
        print("Successful")
        break
else:
        print("Attempted 3 times and fail")


#Nested loops

for x in range(5):
     for y in range(3):
          print(f"({x}, {y})")


print(type(45))
print(type(range(5)))

for x in [1,2,3,4,5]:
     print(x, end =" ")
count = 0
for number in range(1,10):
    if number % 2 == 0:
        count += 1
        print(number)

print(f"we have{count} even numbers")


           #assaignment.
#creating a list of number
#variable is total =0
# use for loop
# inside the loop add the current number to the total variable
# print the final total value which represent the sum of all numbers

total = 0
numbers =[1,5,3,9]
for numbers in  range(8):
    total +=1
    print(numbers)
print(f"the sum of the numbers is{numbers}")

         
