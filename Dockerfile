FROM python:3.7-alpine
ENV PYTHONBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser user
USER user