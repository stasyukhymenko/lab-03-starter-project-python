FROM python:3.12.2

WORKDIR /app

COPY backend.txt /app

RUN python -m venv ./.venv

RUN . ./.venv/bin/activate

RUN pip install -r backend.txt --no-deps

COPY spaceship /app
COPY build /app

CMD uvicorn spaceship.main:app --host=0.0.0.0 --port=8080