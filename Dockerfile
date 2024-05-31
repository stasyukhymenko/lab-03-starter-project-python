FROM python:3.10-buster

WORKDIR /app

COPY backend.txt /app

RUN python -m venv ./.venv

RUN . ./.venv/bin/activate

RUN pip install -r backend.txt --no-deps

COPY spaceship /app/spaceship
COPY build /app/build

CMD uvicorn spaceship.main:app --host=0.0.0.0 --port=8080