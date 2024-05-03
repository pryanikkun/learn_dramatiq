import logging
import sys
import asyncio

from aiogram.types import Message
from aiogram.filters import CommandStart
from src.config import dp, bot
from dramatiq_.services import send_msg_from_tg


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer("Привет! Пиши :)")


@dp.message()
async def ticket_message(message: Message):
    user = message.from_user
    text = message.text
    task = send_msg_from_tg.send(text=text, chat_id=user.id)
    print(f"{user=} {text=}")


async def main():
    await dp.start_polling(bot, relax=0.5, polling_timeout=250)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    # dp.run_polling(bot)




