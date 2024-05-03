from sqlalchemy import Column, Integer, Text, String, DateTime, \
    ForeignKey, func
from database import Base


class Employee(Base):
    __tablename__ = 'employees'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(length=200))
    password = Column(String(length=200))
    first_name = Column(String(length=200))
    last_name = Column(String(length=200))


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(length=200))
    chat_id = Column(Integer, index=True)


class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String(length=200))
    ticket_date = Column(DateTime(timezone=True), default=func.now())
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    employee_id = Column(Integer, ForeignKey('employees.id'),  nullable=False)


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    ticket_id = Column(Integer, ForeignKey('tickets.id'),  nullable=False)
