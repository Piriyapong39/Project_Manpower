FROM python:3.11.9-alpine3.19

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt


