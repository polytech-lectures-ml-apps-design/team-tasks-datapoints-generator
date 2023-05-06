FROM python:3.10-alpine
LABEL authors="nicolay"

COPY producer.py .
COPY requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "./producer.py"]

