score = eval(input("enter your scores: "))

if score in range(95,100):
    grade = "A"
elif score in range(80,94):
    grade = "A-"
elif score in range(70,79):
    grade = "B+"
elif score in range(63,69):
    grade = "B"
elif score in range(55,62):
    grade = "B-"
elif score in range(46,54):
    grade = "C+"
elif score in range(30,45):
    grade = "D"
else:
    grade = "E"

print("Your grade is",grade)


#basic syntax of Match case statement

day = input("Enter the day of the week!")

match day:
    case "Monday":
        print("ugh,Mondays are boring...")
    case "tuesday":
        print("just another day of work!")
    case "wednesday":
        print("Hump day and almost end!")
    case "thursday":
        print("Almost there!")
    case "friday":
        print("TGIF")
    case "saturday:" | "sunday":
        print("Weekend vibes!")
    case _:
        print("invalid input:")


# Matching data types:
value = input("enter a value(number or string):")

match value:
    case int():
        print("You have entered an integer",value)
    case str():
        print("You have entered a string",value)
    case bool():
        print("you have entered a boulean value",value)
    case _:
        print("invalid input",value)

# A list example
fruits = ["apple","mangoe","orange"]

for fruit in fruits:
    print(fruit)
print(f"This is how we access data in a list: {fruits[1]}")