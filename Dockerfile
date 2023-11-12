FROM python:3.11.6-slim-bullseye

ENV PYTHONUNBUFFERED = 1

RUN apt-get update && apt-get -y install gcc libpq-dev

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app/