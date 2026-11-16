from product import Product

class OrderLine:
    def __init__(self, product : Product, quantity : int) -> None:
        if quantity <= 0:
            raise ValueError("Order quantity must be greater than zero.")
        self.product : Product = product
        self.quantity : int = quantity

    def calculate_subtotal(self) -> float:
        return self.product._price * self.quantity
    
    def display_line(self) -> None:
        print(f"Product ordered: {self.product._name} | Quantity: {self.quantity}")