from sqlalchemy.orm import Session

from app import models,schemas

"""
crud.py

Functions:
    create_task() - Create a new task.
    get_tasks()   - Retrieve all tasks with pagination.
    get_task()    - Retrieve a task by ID.
    update_task() - Update an existing task.
    delete_task() - Delete a task.
"""


# create a new task in the database

def create_task(db:Session,task:schemas.TaskCreate):

    db_task = models.Task(title=task.title.strip(),description=task.description)

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


# get all tasks from the database

def get_tasks(db:Session,skip:int = 0,limit:int = 100):
    return(db.query(models.Task).offset(skip).limit(limit).all() )


# get one task by its ID
def get_task(db:Session,task_id:int):

    return(db.query(models.Task).filter(models.Task.id == task_id).first())


#Update an existing task

def update_task(db:Session,db_task:models.Task,task_update:schemas.TaskUpdate):

    update_data = task_update.model_dump(exclude_unset = True)

    if "title" in update_data and update_data['title'] is not None:
        update_data['title'] = update_data['title'].strip()


    for field,value in update_data.items():
        setattr(db_task,field,value)


    db.commit()
    db.refresh(db_task)

    return db_task


# delete an existing task

def delete_task(db:Session,db_task:models.Task):
    db.delete(db_task)
    db.commit()
    return True 




