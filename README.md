# LMS API (Система управления обучением)

Проект представляет собой бэкенд-сервер для онлайн-платформы обучения. Реализован на Django с использованием
Django REST Framework (DRF). Позволяет управлять курсами, уроками и пользователями, предоставляя REST API для
SPA-приложений.

## Основные возможности

- Модели пользователя (кастомная, авторизация по email) с полями: телефон, город, аватар.
- Модели курса и урока: курсы содержат название, описание, превью (картинка); уроки — название, описание, превью,
- ссылку на видео, привязку к курсу.
- Полный CRUD для курсов (ViewSet) и для уроков (Generic-классы).
- Эндпоинт для просмотра и редактирования профиля пользователя (Generic RetrieveUpdateAPIView).
- Поддержка загрузки изображений (Pillow).
- Подключение PostgreSQL (или SQLite для разработки).
- Управление через админ-панель Django (суперпользователь).
- Настройка переменных окружения через `.env` (секретный ключ, параметры БД и т.д.).

## Технологии

- Python 3.13
- Django 6.0.5
- Django REST Framework 3.17.1
- PostgreSQL / psycopg2-binary
- Pillow (для работы с изображениями)
- python-dotenv
- Poetry (управление зависимостями)

## Установка и запуск

### 1. Клонируйте репозиторий и перейдите в папку проекта:
   ```
   git clone https://github.com/Margarita2405/Project12-Skypro-Django-DRF
   cd Project12-Skypro-Django-DRF
   ```
   
### 2. Создайте базу данных PostgreSQL

CREATE DATABASE django_drf;

### 3. Создайте файл .env в корне проекта (по примеру .env.example):

```
SECRET_KEY=your_secret_key_here

DEBUG=True

# НАСТРОЙКИ ПОДКЛЮЧЕНИЯ К PostgreSQL
DATABASE_NAME=django_drf
DATABASE_USER=your_user_name
DATABASE_PASSWORD=your_password
DATABASE_HOST=localhost
DATABASE_PORT=5432

# GITHUB TOKEN
# Personal Access Token для GitHub
# Создайте на: https://github.com/settings/tokens
# Необходимые scope: repo, read:org, user (в зависимости от нужд)
GITHUB_TOKEN=your_github_token_here
```

### 4. Создайте и примените миграции

```
python manage.py makemigrations
python manage.py migrate
```

### 5. Создайте суперпользователя

```
python manage.py createsuperuser
```

### 6. Запуск сервера разработки
```
python manage.py runserver
Проект будет доступен по адресу: http://127.0.0.1:8000
```
## API Эндпоинты

**Курсы (ViewSet)**

- GET	/lms/courses/	Список всех курсов (включая вложенные уроки)
- POST	/lms/courses/	Создание нового курса
- GET	/lms/courses/{id}/	Детальная информация о курсе
- PUT/PATCH	/lms/courses/{id}/	Обновление курса
- DELETE	/lms/courses/{id}/	Удаление курса
- Пример тела POST-запроса на создание курса:
```
json
{
    "title": "Python для начинающих",
    "description": "Курс по основам Python",
    "preview": null
}
```

**Уроки (Generic)**

- GET	/lms/lessons/	Список всех уроков
- POST	/lms/lessons/create/	Создание нового урока (обязательные поля: title, course)
- GET	/lms/lessons/{id}/	Детальный просмотр урока
- PUT/PATCH	/lms/lessons/update/{id}/	Обновление урока
- DELETE	/lms/lessons/delete/{id}/	Удаление урока
- Пример тела POST-запроса на создание урока:
```
json
{
    "title": "Установка Python",
    "description": "Как установить Python на Windows, macOS и Linux",
    "course": 1,
    "video_url": "https://www.youtube.com/watch?v=example"
}
```

**Пользователи (профиль)**

- GET	/users/profile/{id}/	Получение информации о пользователе
- PUT/PATCH	/users/profile/{id}/	Редактирование профиля (поля: first_name, last_name, phone, city, avatar)
- Пример обновления профиля:
```
json
{
    "first_name": "Иван",
    "phone": "+7-999-123-4567",
    "city": "Москва"
}
```

## Админ-панель

Админка доступна по адресу /admin/. В ней можно управлять пользователями, курсами, уроками.

## Статические и медиа-файлы

- Статические файлы (CSS, JS) собираются в папке static/ (создаётся автоматически).

- Медиа-файлы (аватарки, превью) сохраняются в media/.

## Тестирование API

Рекомендуется использовать Postman или любой другой REST-клиент. Убедитесь, что установлен Content-Type:
application/json для POST/PUT/PATCH запросов.

## Документация:

Для получения дополнительной информации обратитесь 
к [документации](README.md).

## Лицензия

Проект выполнен в рамках курсовой работы. Свободное использование только в учебных целях.

## Контакты
Разработчик: Буршева Маргарита

Email: mbursheva@mail.ru

Проект: https://github.com/Margarita2405/Project12-Skypro-Django-DRF
