from datetime import date

class Calculator:
    def __init__(self,version:int):
        self.version = version

    def description(self):
        print(f"Currently we are running the calculator on version: {self.version}")
    
    def add_numbers(self, *numbers:float):
        return sum(numbers)
    

if __name__ == "__name__":

    calc1 = Calculator(10)
    calc2 = Calculator(200)

    calc1.description()
    calc2.description()


    print(Calculator.add_numbers(10, 20, 30))

# def divide(y,x):
#     if x == 0:
#         raise ZeroDivisionError("Division by zero is not allowed!")
#     return y / x
# divide(3,0)