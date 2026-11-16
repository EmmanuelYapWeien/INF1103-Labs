from order_line import OrderLine
from product import Product
from discount_strategy import DiscountStrategy
from no_discount import NoDiscount

class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy | None = None) -> None:
        self.order_id : str = order_id
        self.order_lines : list[OrderLine] = []
        self.discount : DiscountStrategy = discount if discount is not None else NoDiscount()

    def set_discount(self, discountStrat: DiscountStrategy) -> None:
        self.discount = discountStrat

    def add_order_line(self, product : Product, quantity : int) -> None:
        order_line : OrderLine = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def remove_order_line(self, product_id : str) -> None:
        for index, line in enumerate(self.order_lines):
            if(line.product._product_id == product_id):
                self.order_lines.pop(index)
                print("\nProduct removed successfully!\n")

    def calculate_total(self) -> float:
        total : float = 0
        for orderLine in self.order_lines:
            total += orderLine.calculate_subtotal()
        print(f"Total value of Order: ${total}")
        return self.discount.apply(total)

    def display_order(self) -> None:
        for line in self.order_lines:
            line.display_line()
        self.calculate_total()