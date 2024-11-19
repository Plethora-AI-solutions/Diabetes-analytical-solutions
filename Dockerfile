FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip

COPY require.txt require.txt

RUN pip install --no-cache-dir -r require.txt

COPY . /app

CMD [ "gunicorn", "--bind", "0.0.0.0:8080", "PredictDai.wsgi"]