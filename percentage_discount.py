from discount_strategy import DiscountStrategy

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent : float) -> None:
        self.percent = percent
    def apply(self, total : float) -> float:
        return total * (1 - self.percent / 100)