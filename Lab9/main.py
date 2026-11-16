from pathlib import Path
import tempfile

from product import Product
from inventory import Inventory
from file_handling import FileHandling
from supplier import Supplier
from order import Order
from bulk_discount import BulkDiscount
from percentage_discount import PercentageDiscount
from product_factory import ProductFactory
from product_loader import load_products
from student_discount import StudentDiscount
from user_input import get_non_negative_int, get_positive_float

def get_valid_input() -> int:
    while True:
        try:
            option = int(input("Enter Option: "))
        except ValueError:
            print("Please enter a valid menu option.")
            continue
        if 1 <= option <= 13:
            return option
        print("Please enter an option from 1 to 13.")

def productDetails(value : int) -> str | tuple:
    productID = input("ProductID: ")
    if(value == 2):
        supplier_id = input("Supplier ID: ")
        supplier_name = input("Supplier Name: ")
        supplier_email = input("Supplier Contact Email: ")
        supplier = Supplier(supplier_id, supplier_name, supplier_email)
        typeOfProduct = input("Please choose product type(Physical or Digital): ")
        name = input("Product Name: ")
        price = get_positive_float("Price: ")
        stock = get_non_negative_int("Stock Quantity: ")
        return (typeOfProduct, productID, name, price, stock, supplier)
    return productID

def chooseInventory() -> Inventory:
    print("Choose Inventory to work with:")
    print("1. Inventory A")
    print("2. Inventory B")
    while True:
        try:
            choice = int(input("Enter your choice (1 or 2): "))
        except ValueError:
            print("Please enter a valid inventory choice.")
            continue
        if choice == 1:
            return inventory_A
        if choice == 2:
            return inventory_B
        print("Invalid choice. Please choose Inventory 1 or 2.")

def show_product_details(product : Product) -> None:
    product.display_information()
    print(product.get_fulfillment_info())

def run_lab_checks() -> None:
    results = []

    def check(description: str, passed: bool) -> None:
        results.append(passed)
        print(f"{'PASS' if passed else 'FAIL'}: {description}")

    supplier = Supplier("S1", "Test Supplier", "test@example.com")
    product = ProductFactory.create(
        "physical", "P1", "Test Product", 250, 1, supplier
    )
    order = Order("O1", BulkDiscount(200, 20))
    order.add_order_line(product, 1)
    check("BulkDiscount gives a total of 230", order.calculate_total() == 230)
    order.set_discount(PercentageDiscount(10))
    check("set_discount changes the total to 225", order.calculate_total() == 225)
    check("NoDiscount keeps the total at 250", Order("O2").discount.apply(250) == 250)

    shared_discount = PercentageDiscount(10)
    first_order = Order("O3", shared_discount)
    second_order = Order("O4", first_order.discount)
    check("Two orders can share a discount strategy", first_order.discount is second_order.discount)

    physical = ProductFactory.create("Physical", "P2", "Desk", 10, 0, supplier, 3)
    digital = ProductFactory.create("digital", "D1", "File", 10, 0, supplier, 5)
    check("ProductFactory creates physical and digital products",
          physical._type == "Physical" and digital._type == "Digital")

    try:
        ProductFactory.create("service", "S1", "Setup", 10, 0, supplier)
    except ValueError as error:
        check("Unknown product type raises ValueError", "service" in str(error))
    else:
        check("Unknown product type raises ValueError", False)

    for price in (0, -1, float("nan"), float("inf")):
        try:
            ProductFactory.create("physical", "P3", "Desk", price, 0, supplier)
        except ValueError:
            check(f"Invalid price {price} is rejected", True)
        else:
            check(f"Invalid price {price} is rejected", False)

    try:
        ProductFactory.create("physical", "P4", "Desk", 10, -1, supplier)
    except ValueError:
        check("Negative stock is rejected", True)
    else:
        check("Negative stock is rejected", False)

    try:
        product.update_stock(-1)
    except ValueError:
        check("Negative stock updates are rejected", True)
    else:
        check("Negative stock updates are rejected", False)

    for quantity in (0, -1):
        try:
            Order("O5").add_order_line(product, quantity)
        except ValueError:
            check(f"Invalid order quantity {quantity} is rejected", True)
        else:
            check(f"Invalid order quantity {quantity} is rejected", False)

    student_order = Order("O6", StudentDiscount())
    student_order.add_order_line(product, 1)
    check("StudentDiscount is a separate strategy",
          student_order.calculate_total() == 237.5)

    inventory = Inventory()
    load_products(
        str(Path(__file__).resolve().with_name("products.csv")),
        inventory,
        supplier,
    )
    loaded_ids = [item._product_id for item in inventory.products]
    check("Valid CSV rows load and invalid rows are skipped",
          loaded_ids == ["P001", "D001", "P003"])

    missing_inventory = Inventory()
    with tempfile.TemporaryDirectory() as directory:
        missing_path = str(Path(directory) / "missing.csv")
        load_products(missing_path, missing_inventory, supplier)
    check("Missing CSV file is handled without crashing",
          len(missing_inventory.products) == 0)

    print(f"\n{sum(results)} of {len(results)} checks passed.")
    print("Manual input check: enter invalid text or out-of-range values at the prompts.")


test_supplier : Supplier = Supplier("S999", "George Washington", "Washington@founder.com")
test_product : Product = ProductFactory.create("Physical", "P100", "USB", 99.99, 9999999, test_supplier, 2)
test_product2 : Product = ProductFactory.create("Digital", "P101", "lab.docx", 15.25, 100, test_supplier, 57)
inventory_A :Inventory = Inventory() # creating the inventory object from the Inventory class
inventory_B : Inventory = Inventory() # creating the inventory object from the Inventory class  

percentDiscount : PercentageDiscount = PercentageDiscount(10)
bulkDiscount : BulkDiscount = BulkDiscount(200,20)

order_A : Order = Order("O001", percentDiscount)
order_B : Order = Order("O002", bulkDiscount)

fileHandling : FileHandling = FileHandling()

fileHandling.initialize(inventory_A, "Inventory_A")
fileHandling.initialize(inventory_B, "Inventory_B")
userInput : int = get_valid_input()

while(userInput != 13):
    if(userInput == 10):
        print("Testing Order and DiscountStrategy relationship")
        shared_order : Order = Order("O004", order_A.discount)
        print(f"Order A and O004 share the same PercentageDiscount object: {order_A.discount is shared_order.discount}")
        print("Relationship: Association (an Order uses a DiscountStrategy).")
        print("Multiplicity: each Order has 1 DiscountStrategy; each DiscountStrategy can serve 0..* Orders.")
        userInput = get_valid_input()
        continue
    if(userInput == 9):
        print("Running implementation checks")
        run_lab_checks()
        userInput = get_valid_input()
        continue
    if(userInput == 12):
        inventory = chooseInventory()
        load_products("products.csv", inventory, test_supplier)
        userInput = get_valid_input()
        continue
    inventory : Inventory = chooseInventory()
    if(userInput == 1):
        inventory.display_all()
    elif(userInput == 11):
        print("\nSaving Inventory...")
        fileHandling.save_inventory(inventory_A)
        fileHandling.save_inventoryB(inventory_B)
        print("Inventory saved successfully to inventory.json.\n")
    else:
        productInfo : str | tuple = (
            "" if userInput in (8, 9) else productDetails(userInput)
        )
        if(isinstance(productInfo, tuple)):
            typeOfProduct, productID, name, price, stock, supplier = productInfo
        if(userInput == 2):
            print("\nAdd New Product")
            extra_info = 0
            if(typeOfProduct.strip().lower() == "physical"):
                extra_info = get_non_negative_int("Weight: ")
            elif(typeOfProduct.strip().lower() == "digital"):
                extra_info = get_non_negative_int("Data Size(in MB): ")
            try:
                product = ProductFactory.create(
                    typeOfProduct,
                    productID,
                    name,
                    price,
                    stock,
                    supplier,
                    extra_info
                )
            except ValueError as error:
                print(f"Product could not be added: {error}")
            else:
                print("Supplier Details:")
                product.display_supplier_info()
                inventory.add_product(product)
        elif(userInput == 3):
            print("\nUpdate Stock")
            product : Product | None = inventory.search_product(productInfo)
            if product is not None:
                quantity = get_non_negative_int("\nNew Stock Quantity: ")
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