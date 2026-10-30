import json
from product import Product
fileName = "inventory.json"

class FileHandling:
    def initialize(self, inventory):
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

    def save_inventory(self, inventory):
        data = []
        for product in inventory.products:
            data.append({
                "ID": product._Product__product_id,
                "Name": product._Product__name,
                "Price" : product._Product__price,
                "Stock" : product._Product__stock
            })
        with open(fileName, "w") as file:
            json.dump(data, file, indent=4)
