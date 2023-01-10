FROM python:3.9.6-alpine

ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
WORKDIR /app

RUN apk add --no-cache git

COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir

COPY . ./
EXPOSE 8000
