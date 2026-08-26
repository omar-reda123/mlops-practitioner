FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

COPY pyproject.toml uv.lock README.md* ./

RUN uv sync --no-dev --no-install-project

COPY src ./src
COPY models ./models

RUN uv sync --no-dev

EXPOSE 8000

CMD ["uv","run","uvicorn","prodml.api.main:app","--host","0.0.0.0","--port","8000"]
