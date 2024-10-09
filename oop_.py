#Tring the object oriented programming classes and objects

class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

        def increment_odometer(self,miles):
            self.odometer_reading += miles

my_car = car("BMW", "X5" , 2023)




class cow:
    def __init__(self, name, breed, age, country):
        self.name = name
        self.breed = breed
        self.age = age
        self.country = country

    def dog(self, slang):
        self.slang = slang

    def bark(self):
        return " woof! woof! woof!"
    

chase1 = cow("Helida","freshian", 5, "Germany")
chase2 = cow("Adhiambo", "Gready", 3, "Greece")

print(f"{chase1.name}, is a cow breed called {chase1.breed} and chased with jarry while barking{chase1.bark()}")
print(f"{chase2.name},is a cheeky breed of {chase2.breed}")

class student:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    

student1 =student("Akello", 20)

print(f"{student1.name} was seen playing with children at his older age {student1.age}")

print(f"{student1.name} was called with him!")