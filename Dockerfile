FROM python:3.11-slim
WORKDIR /usr/src/app
COPY main.py .
COPY can_be_shipped.py .
COPY digital_product.py .
COPY physical_product.py .
COPY discount_strategy.py .
COPY file_handling.py .
COPY inventory.py .
COPY product.py .
COPY no_discount.py .
COPY inventory.json .
COPY supplier.py .
COPY order.py .
COPY order_line.py .
COPY bulk_discount.py .
COPY percentage_discount.py .
COPY product_loader.py .
COPY product_factory.py .
COPY products.csv .
COPY student_discount.py .
COPY user_input.py .
CMD ["python", "main.py"]