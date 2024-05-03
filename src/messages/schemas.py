from pydantic import BaseModel


class ViewMessage(BaseModel):
    id: int
    ticket_id: int
    text: str


class CreateMessage(BaseModel):
    ticket_id: int
    text: str
