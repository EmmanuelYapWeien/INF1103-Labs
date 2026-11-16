import math
from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):
    def __init__(self, type : str, productID : str, name : str, price : float, stock : int, supplier : Supplier) -> None:
        if not math.isfinite(price) or price <= 0:
            raise ValueError("Product price must be greater than zero.")
        if stock < 0:
            raise ValueError("Stock quantity cannot be negative.")
        self._type : str = type
        self._product_id : str = productID
        self._name : str = name
        self._price : float = price
        self._stock : int = stock
        self._supplier : Supplier = supplier

    def update_stock(self, quantity : int) -> None:
        if quantity < 0:
            raise ValueError("Stock quantity cannot be negative.")
        self._stock : int = quantity
        print("\nStock updated successfully!\n")

    def display_information(self) -> None:
            print(f"Type: {self._type} | ID: {self._product_id} | Name: {self._name} | Price: ${self._price} | Stock: {self._stock}")

    def display_supplier_info(self) -> None:
        self._supplier.display_information()

    @abstractmethod
    def get_fulfillment_info(self) -> None:
        pass