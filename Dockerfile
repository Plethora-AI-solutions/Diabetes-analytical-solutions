FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["gunicorn", "--bind" ,":$PORT", "--workers 1", "--threads 8","--timeout  0", "main:PredictDai"]
