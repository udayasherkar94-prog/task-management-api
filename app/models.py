from sqlalchemy import Column,Integer,String,Text,Boolean,DateTime
from sqlalchemy.sql import func


from app.database import Base

# Task table definition

class Task(Base):
    __tablename__ = "tasks"

    # unique id for each task

    id = Column(Integer,primary_key = True,index = True)

    # title (required)
    title = Column(String(200),nullable=False)

    #task compeletion status default false
    completed = Column(Boolean,default=False,nullable=False)


    #Automatically store task creation time
    created_at = Column(DateTime(timezone=True),server_default=func.now())


    # automatically update time when the task is modified

    updated_at = Column(DateTime(timezone=True), server_default=func.now(),onupdate=func.now())

    


