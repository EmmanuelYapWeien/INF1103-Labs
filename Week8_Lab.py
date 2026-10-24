import json
fileName = "inventory.json"

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
        if(userInput == 1):
            print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price} | Stock: {self.__stock}")
        elif(userInput == 4):
            print("\nProduct Found:\n-------------------------")
            print(f"ID: {self.__product_id}\nName: {self.__name}\nPrice: ${self.__price}\nStock: {self.__stock}")
            print("-------------------------\n")

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product, announce=True):
        self.products.append(product)
        if announce:
            print("\nProduct added successfully!\n")

    def search_product(self, productID):
        for product in self.products:
            if(product._Product__product_id == productID):
                if(userInput == 3):
                    print("\nProduct Found:")
                    print(f"Name: {product._Product__name}")
                    print(f"Current Stock: {product._Product__stock}")
                return product
        print("\nProduct not found.\n")
        return None
        
    def display_all(self):
        print("\nCurrent Inventory:\n-------------------------")
        for products in self.products:
            products.display_information()
        print("-------------------------\n")

def initialize():
    print("===================================\nINVENTORY MANAGEMENT SYSTEM\n===================================\n")
    try:
        with open(fileName, "r") as file:
            print("inventory.json file found.")
            data = json.load(file)
            for item in data:
                product = Product(item["ID"], item["Name"], item["Price"], item["Stock"])
                inventory.add_product(product, announce=False)
            print("Inventory loaded successfully.\n")
    except FileNotFoundError:
        with open(fileName, "a") as file:
            print("inventory.json file created.")
    print("----------MENU----------\n1. Display All Products\n2. Add Product\n3. Update Stock\n4. Search Product\n5. Save Inventory\n6. Exit\n------------------------\n")

def save_inventory(inventory):
    data = []
    for product in inventory.products:
        data.append({
            "ID": product._Product__product_id,
            "Name": product._Product__name,
            "Price" : product._Product__price,
            "Stock" : product._Product__stock
        })
    if(userInput == 5):
        print("\nSaving Inventory...")
        with open(fileName, "w") as file:
            json.dump(data, file, indent=4)
        print("Inventory saved successfully to inventory.json.\n")
    elif(userInput == 6):
        print("\nSaving Inventory before exit...")
        with open(fileName, "w") as file:
            json.dump(data, file, indent=4)
        print("Inventory saved successfully.\n\nThank you for using the Inventory Management System.\nProgram terminated.")

def get_valid_input():
    option = int(input("Enter Option: "))
    return option

inventory = Inventory() # creating the inventory object from the Inventory class

initialize()
userInput = get_valid_input()

while(userInput != 6):
    if(userInput == 1):
        inventory.display_all()
    elif(userInput == 2):
        print("\nAdd New Product")
        productID = input("ProductID: ")
        name = input("Product Name: ")
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
        product = Product(productID, name, price, stock)
        inventory.add_product(product)
    elif(userInput == 3):
        print("\nUpdate Stock")
        productID = input("Enter ProductID: ")
        product= inventory.search_product(productID)
        quantity = int(input("\nNew Stock Quantity: "))
        product.update_stock(quantity)
    elif(userInput == 4):
        print("\nSearch Product")
        productID = input("Enter Product ID: ")
        product = inventory.search_product(productID)
        if(product != None):
            product.display_information()
    elif(userInput == 5):
        save_inventory(inventory)
    userInput = get_valid_input()
save_inventory(inventory)
# product1 = Product("P001", "Laptop", 1200.00, 15)
# product2 = Product("P002", "Mouse", 25.50, 40)

# inventory.add_product(product1) # pass the product to inventory class to store in a list
# inventory.add_product(product2)