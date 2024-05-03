from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from dramatiq_.services import send_answer_from_fast_api
from models.models import Message, Ticket, Client
from .schemas import ViewMessage, CreateMessage
from database import get_async_session


msg_router = APIRouter(prefix="/messages")


@msg_router.get("", response_model=List[ViewMessage])
async def get_message(session: AsyncSession = Depends(get_async_session)):
    query = select(Message)
    result = await session.execute(query)
    return result.all()


@msg_router.get("/{message_id}", response_model=ViewMessage)
async def get_message(message_id: int,
                      session: AsyncSession = Depends(get_async_session)):
    query = select(Message).where(Message.id == message_id)
    result = await session.execute(query)
    return result.all()


@msg_router.post("")
async def post_message_from_employee(new_message: CreateMessage,
                                     session: AsyncSession = Depends(get_async_session)):
    query = select(Ticket).where(Ticket.id == new_message.ticket_id)
    res = await session.execute(query)
    ticket = res.first()
    query = select(Client).where(Client.id == ticket.client_id)
    res = await session.execute(query)
    client = res.first()
    task = send_answer_from_fast_api.send(chat_id=client.chat_id,
                                          text=new_message.text)
    try:
        task_msg_id = task.message_id
        status_msg = 'submitted'
    except AttributeError:
        task_msg_id = None
        status_msg = 'completed'
    stwt = insert(Message).values(new_message.dict())
    await session.execute(stwt)
    return {"status": 201,
            'task_msg_id': task_msg_id,
            'status_msg': status_msg}
