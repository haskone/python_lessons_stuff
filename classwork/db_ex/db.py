import os
import sys
import datetime
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    DateTime,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine('sqlite:///db.db')
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    desc = Column(String(250), nullable=False)
    priority = Column(Integer, nullable=False)
    create_time = Column(DateTime, nullable=False)
    exec_time = Column(DateTime, nullable=False)


def make_task(name, desc, exec_time, priority):
    new_task1 = Task(name=name,
                     desc=desc,
                     create_time=datetime.datetime.utcnow(),
                     exec_time=exec_time,
                     priority=priority)
    session.add(new_task1)
    session.commit()


def get_tasks():
    tasks = session.query(Task).all()
    return [task.name for task in tasks]