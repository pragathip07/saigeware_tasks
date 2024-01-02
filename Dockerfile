FROM python:3.9


ENV PYHTONUNBUFFERED=1
RUN apt-get update \
    && apt-get -y install tesseract-ocr



WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
