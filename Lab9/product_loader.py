import csv

from inventory import Inventory
from product_factory import ProductFactory
from supplier import Supplier


def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    loaded = 0
    try:
        file = open(path, newline="", encoding="utf-8")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        with file:
            rows = csv.reader(file)
            next(rows, None)
            for row_number, row in enumerate(rows, start=2):
                try:
                    if len(row) != 5:
                        raise ValueError(f"Expected 5 columns, got {len(row)}.")
                    product_type, product_id, name, price_text, stock_text = (
                        value.strip() for value in row
                    )
                    product = ProductFactory.create(
                        product_type,
                        product_id,
                        name,
                        float(price_text),
                        int(stock_text),
                        supplier,
                    )
                except ValueError as error:
                    print(f"Skipping row {row_number}: {error}")
                    continue
                inventory.add_product(product, announce=False)
                loaded += 1
            print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")
