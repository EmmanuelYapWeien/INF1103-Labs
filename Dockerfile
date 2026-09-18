FROM python:3.11-slim
WORKDIR /app
COPY modular_auditior.py .
CMD ["python", "modular_auditior.py"]