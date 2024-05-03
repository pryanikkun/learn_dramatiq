import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

load_dotenv()

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

TG_TOKEN = os.environ.get('TG_TOKEN')

RABBITMQ_DEFAULT_USER = os.environ.get('RABBITMQ_DEFAULT_USER')
RABBITMQ_DEFAULT_PASS = os.environ.get('RABBITMQ_DEFAULT_PASS')
RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')
RABBITMQ_PORT = os.environ.get('RABBITMQ_PORT')

DRAMATIQ_BROKER_URL = \
        (f'amqp://{RABBITMQ_DEFAULT_USER}:'
         f'{RABBITMQ_DEFAULT_PASS}@'
         f'{RABBITMQ_HOST}:{RABBITMQ_PORT}/')


bot = Bot(token=TG_TOKEN)
dp = Dispatcher()
