# digital_product.py
# Child class
from product import Product

class DigitalProduct(Product):
    def __init__(self, type, productID, name, price, stock, download_size):
        super().__init__(type, productID, name, price, stock)
        self._download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Size: {self._download_size}MB")

    def get_fulfillment_info(self):
        print("Product is delivered digitally")