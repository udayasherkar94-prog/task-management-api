from datetime import datetime
from typing import Optional

from pydantic import BaseModel,ConfigDict,Field
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


# field return by the API

class TaskResponse(BaseModel):
    id:int
    title:str
    description:Optional[str] = None
    completed : bool
    created_at : datetime
    updated_at :Optional[datetime] = None
