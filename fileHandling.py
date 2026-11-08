import json
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier
from inventory import Inventory
fileName = "inventory.json"

class FileHandling:
    def initialize(self, inventory : Inventory, inventory_key : str =None) -> None:
        if(inventory_key == "Inventory_A"):
            print("===================================\nINVENTORY MANAGEMENT SYSTEM\n===================================\n")
        try:
            with open(fileName, "r") as file:
                print("inventory.json file found.")
                data : dict = json.load(file)
                if isinstance(data, dict):
                    if inventory_key:
                        products : list[dict] = data.get(inventory_key, [])
                    else:
                        products : list[dict] = data.get("Inventory_A", [])
                else:
                    products : dict = data

                for item in products:
                    supplier : None | Supplier = None
                    if "Supplier_ID" in item:
                        supplier : None | Supplier = Supplier(
                            item["Supplier_ID"],
                            item["Supplier_Name"],
                            item["Supplier_Email"]
                        )
                    if(item["Type"] == "Physical"):
                        product : PhysicalProduct | DigitalProduct = PhysicalProduct(item["Type"], item["ID"], item["Name"], item["Price"], item["Stock"], supplier, item["Weight"])
                    elif(item["Type"] == "Digital"):
                        product :PhysicalProduct | DigitalProduct = DigitalProduct(item["Type"], item["ID"], item["Name"], item["Price"], item["Stock"], supplier, item["Size"])
                    inventory.add_product(product, announce=False)
                print(f"{inventory_key} loaded successfully.\n")
        except FileNotFoundError:
            with open(fileName, "a") as file:
                print("inventory.json file created.")
        except json.decoder.JSONDecodeError:
            print("inventory.json empty")
        if(inventory_key == "Inventory_B"):
            print("----------MENU----------\n1. Display All Products\n2. Add Product\n3. Update Stock\n4. Search Product\n5. Remove Product\n6. Testing Aggregation\n7. Testing Composition\n8. Task 6\n9. Save Inventory\n10. Exit\n------------------------\n")

    def save_inventory(self, inventory : Inventory):
        self._save_inventory_key(inventory, "Inventory_A")

    def save_inventoryB(self, inventory : Inventory):
        self._save_inventory_key(inventory, "Inventory_B")

    def _save_inventory_key(self, inventory : Inventory, inventory_key : str):
        data_dict : dict = {}
        data : list = []
        for product in inventory.products:
            supplier : Supplier = product._supplier
            if(hasattr(product, "_weight")):
                data.append({
                    "Type": "Physical",
                    "ID": product._product_id,
                    "Name": product._name,
                    "Price" : product._price,
                    "Stock" : product._stock,
                    "Weight" : product._weight,
                    "Supplier_ID" : supplier._supplier_id,
                    "Supplier_Name" : supplier._name,
                    "Supplier_Email" : supplier._contact_info
                })
            elif(hasattr(product, "_download_size")):
                data.append({
                    "Type": "Digital",
                    "ID": product._product_id,
                    "Name": product._name,
                    "Price" : product._price,
                    "Stock" : product._stock,
                    "Size" : product._download_size,
                    "Supplier_ID" : supplier._supplier_id,
                    "Supplier_Name" : supplier._name,
                    "Supplier_Email" : supplier._contact_info
                })
        data_dict[inventory_key] = data

        try:
            with open(fileName, "r") as file:
                saved_data : dict = json.load(file)
                if not isinstance(saved_data, dict):
                    saved_data : dict = {}
        except (FileNotFoundError, json.JSONDecodeError):
            saved_data : dict = {}

        saved_data[inventory_key] = data
        with open(fileName, "w") as file:
            json.dump(saved_data, file, indent=4)