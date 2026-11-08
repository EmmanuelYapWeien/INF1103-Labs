from product import Product


class Inventory:
    def __init__(self) -> None:
        self.products : list[Product] = []

    def add_product(self, product : Product, announce : bool =True) -> None:
        self.products.append(product)
        if announce:
            print("\nProduct added successfully!\n")

    def remove_product(self, productID : str) -> None:
        product : Product | None = self.search_product(productID)
        if(product != None):
            self.products.remove(product)
            print("\nProduct removed successfully!\n")

    def search_product(self, productID : str) -> Product | None:
        for product in self.products:
            if(product._product_id == productID):
                print("\nProduct Found:")
                print(f"Name: {product._name}")
                print(f"Current Stock: {product._stock}")
                return product
        print("\nProduct not found.\n")
        return None
        
    def display_all(self) -> None:
        print("\nCurrent Inventory:\n-------------------------")
        for products in self.products:
            products.display_information()
            print(products.get_fulfillment_info())
        print("-------------------------\n")