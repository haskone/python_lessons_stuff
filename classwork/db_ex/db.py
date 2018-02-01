import os
import sys
import datetime
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    DateTime,
    update,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    desc = Column(String(250), nullable=False)
    priority = Column(Integer, nullable=False)
    create_time = Column(DateTime, nullable=False)
    exec_time = Column(DateTime, nullable=False)


engine = create_engine('sqlite:///db.db')
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()


def update_task(name, desc, exec_time, priority):
    task = session.query(Task).filter_by(
        name=name).first()

    if task is None:
        return False

    task.desc = desc
    task.priority = priority
    task.exec_time = exec_time
    session.add(task)
    session.commit()

    return True


def delete_task():
    pass


def make_task(name, desc, exec_time, priority):
    new_task = Task(name=name,
                    desc=desc,
                    create_time=datetime.datetime.utcnow(),
                    exec_time=exec_time,
                    priority=priority)

    session.add(new_task1)
    session.commit()


def get_tasks():
    tasks = session.query(Task).all()
    return [[task.name, task.desc, task.priority]
            for task in tasks]