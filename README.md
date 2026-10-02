Шаблон проекта на FastAPI

Базовая структура для Python backend-проектов на FastAPI, построенная по слоистой архитектуре.
Стек

    FastAPI — веб-фреймворк

    SQLAlchemy 2.0 async — ORM

    PostgreSQL — база данных

    Pydantic v2 — валидация и схемы

    Alembic — миграции

    pytest — тесты

Архитектура
text

app/
  api/v1/endpoints/   # Роутеры — только принимают запросы и делегируют
  core/               # Конфигурация, безопасность, запуск
  models/             # ORM-модели (SQLAlchemy)
  schemas/            # Схемы запросов/ответов (Pydantic)
  services/           # Бизнес-логика
  repositories/       # Доступ к базе данных
  utils/              # Переиспользуемые вспомогательные функции
tests/
  unit/               # Тестируют сервисы изолированно (без БД)
  integration/        # Тестируют эндпоинты с реальной БД

Как запустить
bash

cp .env.example .env
docker compose up

API доступен по адресу http://localhost:8000
Документация по адресу http://localhost:8000/docs
Тесты
bash

pip install -r requirements.txt
pytest tests/