#list[]
my_list =[20,10,30,40,50]
my_list.append(35)
my_list.remove(35)
print(my_list[::])

list_1=["mango","pinapple", "Guava", "Apple","Orange"]
print(list_1[:1])
name = input("enter name")
dictionry_1 = {
    "Book name":"Half of a yellow sun", 
    "Author": "Chimmamanda Ngozi",
    "Genre":"Fiction"
}
print(type(dictionry_1))

thisdict = dict(name ="Repher", age = 20, country= "Kenya")
print(thisdict)

def greet():
    return "Hello"

def goodbye():
    return "Have nice time, goodbye!"

this_dict = {
    "Greeting": greet,
    "Goodbye": goodbye
}

print(this_dict["Goodbye"]())
print(this_dict["Greeting"]())