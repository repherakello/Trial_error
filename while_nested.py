# age tracker!
age = 0
count = 0
while age < 18:
    age = int(input("Enter your age(must be 18 or older!): "))
    count +=1
    if count == 3:
        print("Expiration of trials!")
        break
    elif count != 3:
        print("you are old enough to proceed")

#guessing game
# import random

# secret_number = random.randint(10,20)

# guess_count = 3
# guess = eval(input("enter your guess from 10 - 20!"))
# while guess != secret_number:
#     guess_count += 1

# print(f"you guessed {guess} in{guess_count} tries!")


outer_count = 5

while outer_count > 0:
    #outer loop controls the number of times the inner loop runs
    inner_count = 1
    while inner_count <= outer_count:
        #inner loop repeats for each outer loop iteration
        print(inner_count, end =" ")
        inner_count += 1
        print() #Move to a new line after each outer loop iteration
        outer_count +=1