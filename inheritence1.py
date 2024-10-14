class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Generic animal sound!")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        print("Woof!")

dog = Dog("Buddy", "Labrador") 
dog.make_sound()   


class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()

class Engine:
    def start(self):
        print("Engine starting...")

car = Car(Engine())
car.start()