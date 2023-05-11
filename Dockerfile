FROM python:3.10.6-slim-bullseye

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.3.0

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN apt update \
    && apt install -y \
    libpq-dev \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install "poetry==$POETRY_VERSION"
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-root --no-ansi

COPY .. .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]