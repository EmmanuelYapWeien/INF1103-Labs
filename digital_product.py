# digital_product.py
# Child class
from product import Product
from supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, type : str, productID : str, name : str, price : float, stock : int, supplier : Supplier, download_size : int) -> None:
        super().__init__(type, productID, name, price, stock, supplier)
        self._download_size : int = download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"Size: {self._download_size}MB")

    def get_fulfillment_info(self) -> None:
        print("Product is delivered digitally")