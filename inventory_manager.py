import json
fileName = "inventory.json"
inventory = []

def initialize():
    print("===================================\nINVENTORY MANAGEMENT SYSTEM\n===================================\n")
    try:
        with open(fileName, "r") as file:
            print("inventory.json file found.")
            inventory.extend(json.load(file))
            print("Inventory loaded successfully.\n")
    except FileNotFoundError:
        with open(fileName, "a") as file:
            print("inventory.json file created.")
    print("----------MENU----------\n1. Display All Products\n2. Add Product\n3. Update Stock\n4. Search Product\n5. Save Inventory\n6. Exit\n------------------------\n")

def display_all():
    print("\nCurrent Inventory:\n-------------------------")
    for product in inventory:
        for key, value in product.items():
            if key != list(product.keys())[-1]:
                print(f"{key}: {value} | ", end="")
            else:
                print(f"{key}: {value}")
    print("-------------------------\n")

def add_product():
    print("\nAdd New Product:")
    product_ID = input("Product ID: ")
    product_name = input("Product Name: ")
    product_price = float(input("Price: "))
    product_stock = int(input("Stock Quantity: "))
    inventory.append({
        "ID": product_ID,
        "Name": product_name,
        "Price": f"${product_price:.2f}",
        "Stock": product_stock
    })
    print("\nProduct added successfully!\n")

def update_stock():
    print("\nUpdate Stock")
    product_ID = input("Enter Product ID: ")
    for product in inventory:
        if product["ID"] == product_ID:
            print(f"\nProduct found:\nName: {product['Name']}\nCurrent Stock: {product['Stock']}")
            new_stock = int(input("New Stock Quantity: "))
            product["Stock"] = new_stock
            print("\nStock updated successfully!\n")

def search_product():
    print("\nSearch Product")
    product_ID = input("Enter Product ID: ")
    for product in inventory:
        if product["ID"] == product_ID:
            print("\nProduct Found\n-------------------------")
            for key, value in product.items():
                print(f"{key}: {value}")
            print("-------------------------\n")
            return
    print("\nProduct not found.\n")
        

def save_inventory():
    if(userInput == 5):
        print("\nSaving Inventory...")
        with open(fileName, "w") as file:
            json.dump(inventory, file, indent=4)
        print("Inventory saved successfully to inventory.json.\n")
    elif(userInput == 6):
        print("\nSaving Inventory before exit...")
        with open(fileName, "w") as file:
            json.dump(inventory, file, indent=4)
        print("Inventory saved successfully.\n\nThank you for using the Inventory Management System.\nProgram terminated.")

def get_valid_input():
    option = int(input("Enter Option: "))
    return option

initialize()
userInput = get_valid_input()

while(userInput != 6):
    if(userInput == 1):
        display_all()
    elif(userInput == 2):
        add_product()
    elif(userInput == 3):
        update_stock()
    elif(userInput == 4):
        search_product()
    elif(userInput == 5):
        save_inventory()
    userInput = get_valid_input()
save_inventory()