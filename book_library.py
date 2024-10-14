import _csv
class Item:
    pay_rate = 0.8 # This is a class attribute and can be accesed in the instances

    all = []   
    def __init__(self, name:str, price:float, quantity):
       #Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"quantity{quantity} is not greater than zero!"
       #Assaign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):# method
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    @classmethod
    def instantiate_from_csv(cls):
        with open('Items.csv', 'r') as f:
            reader = _csv.DictReader
            items = list(reader)
        for item in items:
            print(item)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


Item.instantiate_from_csv()
print(Item.all)

# for instance in Item.all:
#     print(instance.name)

# item1.apply_discount()
# print(item1.price)

# item2.pay_rate = 0.6
# item2.apply_discount()
# print(item2.price)

# print(f"This is item1:{item1.name}")
# print(f"This is item2:{item2.name}")
# print(f"This is item1 quantity:{item1.quantity}")
# print(f"This is item2 quantity:{item2.quantity}")
# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
# print(Item.__dict__)# All attributes for class level
# print(item1.__dict__)#All the attributes for instance level
# print(item2.__dict__)
