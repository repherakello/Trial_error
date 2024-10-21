#Classmethod example work:
class Person:
    count = 0

    def __init__(self,name):
        self.name = name
        Person.count += 1


    @classmethod
    def display_count(cls):
        print(f"The total person's counted are: {cls.count}")

    

person1 = Person("Repher")
person2 = Person("Akello")

Person.display_count()

#StaticMethod example:

class Mathutils:
    @staticmethod
    def add(a,b):
        return a + b
    
    @staticmethod
    def multiply(a,b):
        return a * b
    

print(Mathutils.add(3,4))
print(Mathutils.multiply(3,4))