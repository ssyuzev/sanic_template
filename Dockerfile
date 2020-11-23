FROM python:3.9-slim

RUN mkdir -p /app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD ./src ./src

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-pip \
    build-essential \
    git-core

COPY ./setup.py ./setup.py
COPY ./Pipfile /app/Pipfile

RUN pip install -U pip && pip install -U wheel pipenv
RUN pipenv install -e .
