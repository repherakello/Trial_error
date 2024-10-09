import random
number1 = random.randint(10,25)
number2 = random.randint(10, 25)

if number1 <= number2:
    number1, number2 = number2,number1


count = 0
while count <= 3:
    answer = eval(input("what is "+ str(number1)+ "-"+ str(number2) + "?" ))
    if number1 - number2 == answer:
        print("Awesome guess!")
        break
    elif number1 - number2 != answer:
        count += 1
    if count == 3:
        print("Wrong input!\n", number1, '-', number2, "is", number1 - number2, ".")
    