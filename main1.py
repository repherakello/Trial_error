from math import pi
class Point: #Definig a class
    def __init__(self, x, y): #Constructor of initializing/ method
        self.x = x
        self.y = y

point = Point(3,5) #calling a class by assaigning variable value.
print(f"Point coordinates: ({point.x},{point.y})") #output of the class


# class Circle:
#     def __init__(self,radius):
#         self.radius = radius

#     def getPerimeter(self):
#         return 2 * pi* self.radius
    
#     def getArea(self):
#         return pi * self.radius * self.radius
    
#     def setradius(self, radius):
#         self.radius = radius
    
# Area = Circle(3)
# Perimeter = Circle(15)
# print(f"The area of the circle of radius.{Area.radius} is {Area.getArea()}")
# print(f"The perimeter of a circle of radius, {Perimeter.radius} is {Perimeter.getPerimeter()}")