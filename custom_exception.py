"""Custom exceptions are created to handle specific errors or exceptional situation
Enables deriving specific error message to your application"""
#Creating custom Exception

class custom_error(Exception):
    """Custom exception for handling unavailable staff in the stock"""

    def __init__(self, item_name):
        self.item_name = item_name

    def __str__(self):
        return f"Sorry, the item '{self.item_name}' is currently out of stock."
    
product_inventory = {
    "apple": 10,
    "Banana": 5,
    "Orange": 0,
    "Grapes": 3
    }

def Purchase_item(item, quantity):
    try:
        if product_inventory[item] == 0:
            raise custom_error(item)
        else:
            print(f"Purchase successful: {quantity} {item}(s)")
            product_inventory[item] -= quantity
    except KeyError:
        print(f"Sorry, '{item}' is currently not available in the store! Thank you!")


try:
    Purchase_item("apple", 3)
    Purchase_item("Grapes", 6)
    Purchase_item("Orange", 1)
    Purchase_item("watermelon", 1) #item currently not available in the dict
except custom_error as e:
    print(e)