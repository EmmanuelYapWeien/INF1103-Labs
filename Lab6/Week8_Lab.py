from fileHandling import FileHandling
from inventory import Inventory
from product import Product


def get_valid_input():
    option = int(input("Enter Option: "))
    return option

inventory = Inventory() # creating the inventory object from the Inventory class
fileHandling = FileHandling()

fileHandling.initialize(inventory)
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
        print("\nSaving Inventory...")
        fileHandling.save_inventory(inventory)
        print("Inventory saved successfully to inventory.json.\n")
    userInput = get_valid_input()
print("\nSaving Inventory before exit...")
fileHandling.save_inventory(inventory)
print("Inventory saved successfully.\n\nThank you for using the Inventory Management System.\nProgram terminated.")

# product1 = Product("P001", "Laptop", 1200.00, 15)
# product2 = Product("P002", "Mouse", 25.50, 40)

# inventory.add_product(product1) # pass the product to inventory class to store in a list
# inventory.add_product(product2)