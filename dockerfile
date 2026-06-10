# Используем официальный образ Python
FROM python:3.13-slim

# Отключаем создание .pyc и буферизацию вывода
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Устанавливаем системные зависимости (нужны для psycopg2, Pillow и т.д.)
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Копируем файл с зависимостями Python
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Открываем порт 8000
EXPOSE 8000

# Команда запуска (для разработки используем runserver)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
