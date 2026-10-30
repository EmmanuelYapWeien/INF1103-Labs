class Product:
    def __init__(self, productID, name, price, stock):
        self.__product_id = productID
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, quantity):
        self.__stock = quantity
        print("\nStock updated successfully!\n")

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price} | Stock: {self.__stock}")