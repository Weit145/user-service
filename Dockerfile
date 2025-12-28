# Используем официальный Python
FROM python:3.12-slim

# Системные зависимости (с российским зеркалом Debian, как мы уже делали)
RUN sed -i 's|http://deb.debian.org/debian|http://mirror.yandex.ru/debian|g' /etc/apt/sources.list && \
    sed -i 's|http://security.debian.org/debian-security|http://mirror.yandex.ru/debian-security|g' /etc/apt/sources.list && \
    apt-get update && apt-get install -y --no-install-recommends \
        build-essential libpq-dev curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Poetry
RUN pip install --no-cache-dir poetry==2.2.1

# Настраиваем зеркало PyPI для Poetry
ENV POETRY_PYPI_MIRROR_URL=https://mirror.yandex.ru/mirrors/pypi/simple/

WORKDIR /app

# Копируем зависимости
COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-root

# Копируем весь код
COPY . .

ENV PYTHONPATH="${PYTHONPATH}:/app/proto"

CMD ["poetry", "run", "python", "app/main.py"]