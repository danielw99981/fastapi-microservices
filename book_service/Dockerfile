FROM python:3.11

WORKDIR /app

COPY ./pyproject.toml ./poetry.lock* ./

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install poetry
RUN poetry install

COPY . /app/
