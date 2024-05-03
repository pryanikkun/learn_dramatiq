import dramatiq
import asyncio

from dramatiq.brokers.rabbitmq import RabbitmqBroker
from dramatiq.middleware.asyncio import AsyncIO
from dramatiq.middleware.retries import Retries
from dramatiq.middleware.time_limit import TimeLimit
from dramatiq.worker import Worker
from src.config import DRAMATIQ_BROKER_URL

rabbitmq_broker = RabbitmqBroker(url=DRAMATIQ_BROKER_URL,
                                 middleware=[AsyncIO(), Retries(), TimeLimit()])

dramatiq.set_broker(rabbitmq_broker)

worker = Worker(broker=rabbitmq_broker)
worker.start()
