
""""
schemas.py

Classes:
    TaskCreate   - Validates data for creating a task.
    TaskUpdate   - Validates data for updating a task.
    TaskResponse - Defines the task data returned by the API."""


from datetime import datetime
from typing import Optional

from pydantic import BaseModel,ConfigDict,Field,field_validator
# typing = a module that helps you describe what type of data something is.
# Optional = means “this value can be filled in, or it can be None (empty).
# pydantic = a library (FastAPI uses it internally) that validates data. It checks that incoming data has the right types and rules, and gives clear errors if not.
# ConfigDict
# Used to set settings for a schema. The most common use with SQLAlchemy:



# Field
# Used to add extra rules or information to a single field

class TaskCreate(BaseModel):
    title:str = Field(
        ...,
        min_length = 1,
        max_length = 200,
        description="Title of the task"
    )

    description:Optional[str] = None
    completed :Optional[bool] = None


    @field_validator("title")
    @classmethod
    def validate_title(cls,value:str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Task title cannot be empty or whitespace only")
        return value


# Field allowed when updating a task

class TaskUpdate(BaseModel):
    title:Optional[str] = Field(default = None,min_length=1,max_length=200)
    description:Optional[str] = None
    completed :Optional[bool] = None


    @field_validator("title")
    @classmethod
    def validate_title(cls,value:Optional[str])->Optional[str]:
        if value is None:
            return value
        
        value = value.strip()

        if not value:
            raise ValueError("task title cannot be empty or whitespace only")

        return value

    




# field return by the API

class TaskResponse(BaseModel):
    id:int
    title:str
    description:Optional[str] = None
    completed : bool
    created_at : datetime
    updated_at :Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
    '''
        Setting model_config = ConfigDict(from_attributes=True) in Pydantic v2 allows your Pydantic models to read data directly from arbitrary Python objects and
         ORM models (like SQLAlchemy rows) instead of just dictionaries.
    '''
