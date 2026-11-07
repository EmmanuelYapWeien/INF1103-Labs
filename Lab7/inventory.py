class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product, announce=True):
        self.products.append(product)
        if announce:
            print("\nProduct added successfully!\n")

    def search_product(self, productID):
        for product in self.products:
            if(product._product_id == productID):
                print("\nProduct Found:")
                print(f"Name: {product._name}")
                print(f"Current Stock: {product._stock}")
                return product
        print("\nProduct not found.\n")
        return None
        
    def display_all(self):
        print("\nCurrent Inventory:\n-------------------------")
        for products in self.products:
            products.display_information()
        print("-------------------------\n")