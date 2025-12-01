FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/
COPY templates/ templates/
COPY assets/ assets/
COPY run.sh .
COPY README.md .

ENV DATA_PATH="assets/broadway.csv"

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.app:app"]
