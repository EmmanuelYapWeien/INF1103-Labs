from percentage_discount import PercentageDiscount

class StudentDiscount(PercentageDiscount):
    def __init__(self, percent: float = 5.0) -> None:
        super().__init__(percent)