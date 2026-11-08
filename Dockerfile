FROM python:3.11-slim
WORKDIR /usr/src/app
COPY main.py .
COPY can_be_shipped.py .
COPY digital_product.py .
COPY physical_product.py .
COPY fileHandling.py .
COPY inventory.py .
COPY product.py .
COPY inventory.json .
COPY supplier.py .
COPY order.py .
COPY orderLine.py .
CMD ["python", "main.py"]