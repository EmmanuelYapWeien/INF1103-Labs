# physical_product.py
# Child class
from product import Product
from can_be_shipped import CanBeShipped
from supplier import Supplier

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, type : str, productID : str, name : str, price : float, stock : int, supplier : Supplier, weight : int) -> None:
        super().__init__(type, productID, name, price, stock, supplier)
        self._weight : int = weight

    def get_weight(self) -> int:
        return self._weight
    
    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self._weight}kg")

    def get_fulfillment_info(self) -> None:
        print("Product requires physical shipping")

    def calculate_shipping_cost(self) -> None:
        shippingCost : float = 0.75 * self._weight
        print(f"The cost for shipping is {shippingCost}")