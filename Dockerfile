FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry

RUN poetry config virtualenvs.create false && poetry install --no-dev

COPY . /app

CMD ["poetry", "run", "uvicorn", "testcontainers_fastapi.main:app", "--host", "0.0.0.0", "--port", "8000"]
