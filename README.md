# Dramatiq. FastAPI. Telegram

1. В папке /src нужно создать .env
```
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=

RABBITMQ_DEFAULT_VHOST=
RABBITMQ_DEFAULT_USER=
RABBITMQ_DEFAULT_PASS=
RABBITMQ_HOST=
RABBITMQ_PORT=
TG_TOKEN=
```
2. Проведём миграции с помощью 
```bash
alembic upgrade head
```
3. Поднимем докер
```bash
docker-compose up
```
4. В БД нужно добавить по одной записи в таблицы: `clients` (в поле chat_id нужно внести id чата тг), `employees`, `tickets`

## Запуск
Сначала запускаем `handlers.py`, потом `main.py`.

## Вызов ошибки
Нужно отправить post-запрос на `/messages`, указав id созданного тикета и любой текст.

http://localhost:8000/docs
