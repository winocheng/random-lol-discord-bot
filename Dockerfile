FROM ghcr.io/astral-sh/uv:python3.11-alpine

WORKDIR /app

COPY .  .

RUN uv sync --frozen

CMD ["uv", "run", "bot.py"]