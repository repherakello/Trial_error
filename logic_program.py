#intro to control flow
name = "repher"
age = 55
print(name)
print(age)

#if age >50, access to the system granted
#else if age < 50, permission is not granted

condition_1 = age >= 50
condition_2 = "frontend" 

print(condition_1)

if condition_1:
    print("You have access: ") # works if condition is true!
elif condition_2 == "frontend":
    print("you are \n a rockstar")
else:
    print("you dont have access")# works if condition is not true!

email_e = input("enter your email: \n")
correct_email = "akelloreph@gmail.com"

while email_e != correct_email:
    email_e = input("enter your email: \n")
    pass
    pass
print("success!!!")