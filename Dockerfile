FROM python:3.11-slim
WORKDIR /usr/src/app
COPY Week8_Lab.py .
COPY inventory.json .
CMD ["python", "Week8_Lab.py"]