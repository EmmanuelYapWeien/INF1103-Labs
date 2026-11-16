from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier

class ProductFactory:
    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float,
        stock_quantity: int, supplier: Supplier, extra_info: int = 0) -> Product:
        normalized_type = product_type.strip().lower()
        if normalized_type == "physical":
            return PhysicalProduct("Physical", product_id, name, price, stock_quantity, supplier, extra_info)
        if normalized_type == "digital":
            return DigitalProduct("Digital", product_id, name, price, stock_quantity, supplier, extra_info)
        raise ValueError(f"Unknown product type: {product_type}")

