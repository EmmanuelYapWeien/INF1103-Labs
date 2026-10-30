from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from fileHandling import FileHandling

def get_valid_input():
    option = int(input("Enter Option: "))
    return option

def productDetails(value):
    productID = input("ProductID: ")
    if(value == 2):
        typeOfProduct = input("Please choose product type(Physical or Digital): ")
        name = input("Product Name: ")
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
        return (typeOfProduct, productID, name, price, stock)
    return productID

inventory = Inventory() # creating the inventory object from the Inventory class
fileHandling = FileHandling()

fileHandling.initialize(inventory)
userInput = get_valid_input()

while(userInput != 6):
    if(userInput == 1):
        inventory.display_all()
    elif(userInput == 5):
        print("\nSaving Inventory...")
        fileHandling.save_inventory(inventory)
        print("Inventory saved successfully to inventory.json.\n")
    else:
        productInfo = productDetails(userInput)
        if(isinstance(productInfo, tuple)):
            typeOfProduct, productID, name, price, stock = productInfo
        if(userInput == 2):
            print("\nAdd New Product")
            if(typeOfProduct == "Physical"):
                weight = int(input("Weight: "))
                product = PhysicalProduct(typeOfProduct, productID, name, price, stock, weight)
            elif(typeOfProduct == "Digital"):
                size = int(input("Data Size(in MB): "))
                product = DigitalProduct(typeOfProduct, productID, name, price, stock, size)
            inventory.add_product(product)
        elif(userInput == 3):
            print("\nUpdate Stock")
            product= inventory.search_product(productInfo)
            quantity = int(input("\nNew Stock Quantity: "))
            product.update_stock(quantity)
        elif(userInput == 4):
            print("\nSearch Product")
            product = inventory.search_product(productInfo)
            if(product != None):
                product.display_information()
    userInput = get_valid_input()
print("\nSaving Inventory before exit...")
fileHandling.save_inventory(inventory)
print("Inventory saved successfully.\n\nThank you for using the Inventory Management System.\nProgram terminated.")