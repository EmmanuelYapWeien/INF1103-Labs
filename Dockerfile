FROM python:3.11-slim
WORKDIR /usr/src/app
COPY Week9_Lab.py .
COPY can_be_shipped.py .
COPY digital_product.py .
COPY physical_product.py .
COPY fileHandling.py .
COPY inventory.py .
COPY product.py .
COPY inventory.json .
CMD ["python", "Week9_Lab.py"]