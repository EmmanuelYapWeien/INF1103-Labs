from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, type, productID, name, price, stock):
        self._type = type
        self._product_id = productID
        self._name = name
        self._price = price
        self._stock = stock

    def update_stock(self, quantity):
        self._stock = quantity
        print("\nStock updated successfully!\n")

    def display_information(self):
            print(f"Type: {self._type} | ID: {self._product_id} | Name: {self._name} | Price: ${self._price} | Stock: {self._stock}")

    @abstractmethod
    def get_fulfillment_info(self):
        pass