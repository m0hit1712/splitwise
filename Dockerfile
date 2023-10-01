FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1
RUN mkdir /splitwise
WORKDIR /splitwise

RUN apt-get update && apt-get install -y libpq-dev build-essential

COPY . .

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

EXPOSE 8000
