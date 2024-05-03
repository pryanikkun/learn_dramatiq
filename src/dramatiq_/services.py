import asyncio
import logging
from sqlalchemy import select, insert
from dramatiq_.dramatiq_ import dramatiq
from models.models import Client, Ticket, Message

from messages.schemas import CreateMessage
from database import async_engine
from src.config import dp, bot


def should_retry(retries_so_far, exception):
    return retries_so_far < 3 and isinstance(exception, RuntimeError)


@dramatiq.actor(time_limit=5_000, retry_when=should_retry)
async def send_answer_from_fast_api(text: str, chat_id: int):
    logging.info("Task received!")
    await asyncio.sleep(5)
    await bot.send_message(chat_id=chat_id, text=text)
    logging.info("Task completed!")


@dramatiq.actor()
async def send_msg_from_tg(text: str, chat_id: int):
    async with async_engine.begin() as session:
        logging.info("Task received!")
        query = select(Client).where(Client.chat_id == chat_id)
        result = await session.execute(query)
        client = result.first()
        query = select(Ticket).where(Ticket.client_id == client.id)
        ticket = await session.execute(query)
        ticket = ticket.first()
        msg = CreateMessage(text=text, ticket_id=ticket.id)
        stwt = insert(Message).values(msg.dict())
        await session.execute(stwt)
        logging.info("Task completed!")
