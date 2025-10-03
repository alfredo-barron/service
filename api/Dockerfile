FROM python:3.10-slim

WORKDIR /app

COPY requiements.txt requiements.txt
RUN pip install --no-cache-dir -r requiements.txt

COPY app.py app.py

CMD [ "python", "app.py"]