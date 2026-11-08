from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from fileHandling import FileHandling
from supplier import Supplier
from order import Order

def get_valid_input() -> int:
    option = int(input("Enter Option: "))
    return option

def productDetails(value : int) -> str | tuple:
    productID = input("ProductID: ")
    if(value == 2):
        supplier_id = input("Supplier ID: ")
        supplier_name = input("Supplier Name: ")
        supplier_email = input("Supplier Contact Email: ")
        supplier = Supplier(supplier_id, supplier_name, supplier_email)
        typeOfProduct = input("Please choose product type(Physical or Digital): ")
        name = input("Product Name: ")
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
        return (typeOfProduct, productID, name, price, stock, supplier)
    return productID

def chooseInventory() -> Inventory:
    print("Choose Inventory to work with:")
    print("1. Inventory A")
    print("2. Inventory B")
    choice = int(input("Enter your choice (1 or 2): "))
    if choice == 1:
        return inventory_A
    elif choice == 2:
        return inventory_B
    else:
        print("Invalid choice. Defaulting to Inventory A.")
        return inventory_A

def show_product_details(product : Product) -> None:
    product.display_information()
    print(product.get_fulfillment_info())

test_supplier : Supplier = Supplier("S999", "George Washington", "Washington@founder.com")
test_product : PhysicalProduct = PhysicalProduct("Physical", "P100", "USB", 99.99, 9999999, test_supplier, 2)
test_product2 : DigitalProduct = DigitalProduct("Digital", "P101", "lab.docx", 15.25, 100, test_supplier, 57)
inventory_A :Inventory = Inventory() # creating the inventory object from the Inventory class
inventory_B : Inventory = Inventory() # creating the inventory object from the Inventory class  

order_A : Order = Order("O001")
order_B : Order = Order("O002")

fileHandling : FileHandling = FileHandling()

fileHandling.initialize(inventory_A, "Inventory_A")
fileHandling.initialize(inventory_B, "Inventory_B")
userInput : int = get_valid_input()

while(userInput != 10):
    inventory : Inventory = chooseInventory()
    if(userInput == 1):
        inventory.display_all()
    elif(userInput == 9):
        print("\nSaving Inventory...")
        fileHandling.save_inventory(inventory_A)
        fileHandling.save_inventoryB(inventory_B)
        print("Inventory saved successfully to inventory.json.\n")
    else:
        productInfo : str | tuple = productDetails(userInput)
        if(isinstance(productInfo, tuple)):
            typeOfProduct, productID, name, price, stock, supplier = productInfo
        if(userInput == 2):
            print("\nAdd New Product")
            if(typeOfProduct == "Physical"):
                weight : int = int(input("Weight: "))
                product : PhysicalProduct | DigitalProduct = PhysicalProduct(typeOfProduct, productID, name, price, stock, supplier, weight)
            elif(typeOfProduct == "Digital"):
                size : int = int(input("Data Size(in MB): "))
                product : DigitalProduct | PhysicalProduct = DigitalProduct(typeOfProduct, productID, name, price, stock, supplier, size)
            print("Supplier Details:")
            product.display_supplier_info()
            inventory.add_product(product)
        elif(userInput == 3):
            print("\nUpdate Stock")
            product : Product | None = inventory.search_product(productInfo)
            quantity : int = int(input("\nNew Stock Quantity: "))
            product.update_stock(quantity)
        elif(userInput == 4):
            print("\nSearch Product")
            product : Product | None = inventory.search_product(productInfo)
            if(product != None):
                product.display_information()
        elif(userInput == 5):
            print("\nRemoving Product")
            inventory.remove_product(productInfo)
        elif(userInput == 6):
            print("Testing Aggregation\n")
            print("Adding Test Product to inventory A")
            inventory_A.add_product(test_product)
            print("Removing Test Product from inventory A")
            inventory_A.remove_product(productInfo)
            print("Testing that product still exists even if removed from inventory")
            test_product.display_information()
            print("Adding Test Product to inventory B, if it truly still exists")
            inventory_B.add_product(test_product)
            print("Removing Test Product from inventory B, don't want to save test_product in JSON file")
            inventory_B.remove_product(productInfo)
        elif(userInput == 7):
            print("Composition Task")
            print("Adding product to order_A")
            order_A.add_order_line(test_product, 30)
            order_A.add_order_line(test_product2, 12)
            print("Displaying product in order")
            order_A.display_order()
            print("Adding product to order_B")
            order_B.add_order_line(test_product, 30)
            print("Removing product from order_B")
            order_B.remove_order_line(productInfo)
            order_B.display_order()
        elif(userInput == 8):
            print("Testing Task 6")
            show_product_details(test_product)
            show_product_details(test_product2)
    userInput : int = get_valid_input()
print("\nSaving Inventory before exit...")
fileHandling.save_inventory(inventory_A)
fileHandling.save_inventoryB(inventory_B)
print("Inventory saved successfully.\n\nThank you for using the Inventory Management System.\nProgram terminated.")