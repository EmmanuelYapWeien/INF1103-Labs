# physical_product.py
# Child class
from product import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, type, productID, name, price, stock, weight):
        super().__init__(type, productID, name, price, stock)
        self._weight = weight

    def get_weight(self):
        return self._weight
    
    def display_information(self):
        super().display_information()
        print(f"Weight: {self._weight}kg")

    def get_fulfillment_info(self):
        print("Product requires physical shipping")

    def calculate_shipping_cost(self):
        shippingCost = 0.75 * self._weight
        print(f"The cost for shipping is {shippingCost}")