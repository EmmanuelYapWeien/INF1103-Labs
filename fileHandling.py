import json
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
fileName = "inventory.json"

class FileHandling:
    def initialize(self, inventory):
        print("===================================\nINVENTORY MANAGEMENT SYSTEM\n===================================\n")
        try:
            with open(fileName, "r") as file:
                print("inventory.json file found.")
                data = json.load(file)
                for item in data:
                    if(item["Type"] == "Physical"):
                        product = PhysicalProduct(item["Type"], item["ID"], item["Name"], item["Price"], item["Stock"], item["Weight"])
                    elif(item["Type"] == "Digital"):
                        product = DigitalProduct(item["Type"], item["ID"], item["Name"], item["Price"], item["Stock"], item["Size"])
                    inventory.add_product(product, announce=False)
                print("Inventory loaded successfully.\n")
        except FileNotFoundError:
            with open(fileName, "a") as file:
                print("inventory.json file created.")
        print("----------MENU----------\n1. Display All Products\n2. Add Product\n3. Update Stock\n4. Search Product\n5. Save Inventory\n6. Exit\n------------------------\n")

    def save_inventory(self, inventory):
        data = []
        for product in inventory.products:
            if(hasattr(product, "_weight")):
                data.append({
                    "Type": "Physical",
                    "ID": product._product_id,
                    "Name": product._name,
                    "Price" : product._price,
                    "Stock" : product._stock,
                    "Weight" : product._weight
                })
            elif(hasattr(product, "_download_size")):
                data.append({
                    "Type": "Digital",
                    "ID": product._product_id,
                    "Name": product._name,
                    "Price" : product._price,
                    "Stock" : product._stock,
                    "Size" : product._download_size
                })
            
        with open(fileName, "w") as file:
            json.dump(data, file, indent=4)