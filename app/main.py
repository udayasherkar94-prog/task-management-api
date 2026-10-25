from fastapi import FastAPI,Depends,HTTPException,status
from sqlalchemy.orm import Session 
from typing import List

from app.database import Base,engine,get_db
# from app(module).file  import (functions,classes)


from app import models,crud,schemas

# from module  import file1,file2,file3

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API",
              description="A REST API to manage tasks using FastAPI and Mysql",
              version="1.0.0")


# Home endpoint
@app.get("/")
def home():
    return {"message":"Task Management API is running"}




# create a new task
@app.post("/tasks",
          response_model = schemas.TaskResponse,
          status_code = status.HTTP_201_CREATED)
def create_task(task:schemas.TaskCreate, db:Session = Depends(get_db)):
    if not task.title.strip():

        raise HTTPException(status_code = status.HTTP_422_UNPROCESSABLE_ENTITY,detail="Task title cannot empty")


    return crud.create_task(db,task)




# get all tasks
@app.get("/tasks",response_model = List[schemas.TaskResponse])
def read_tasks(skip: int = 0,limit: int = 100,db:Session = Depends(get_db)):

    if skip < 0 or limit < 1 or limit >100:
        raise HTTPException(status_code = status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="skip must be non-negative and limit must be 1 and 100")


    return crud.get_tasks(db,skip = skip,limit=limit)






# get one task by id

@app.get("/task/{task_id}",response_model=schemas.TaskResponse)
def read_task(task_id : int,db:Session = Depends(get_db)):

    task = crud.get_task(db,task_id)

    if task is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Task not found")

    return task




# Update a task

@app.put("/task/{task_id}",response_model=schemas.TaskResponse)
def update_task(task_id:int,task_update:schemas.TaskUpdate,db:Session = Depends(get_db)):
    task = crud.get_task(db,task_id)

    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not Found")


    if ("title" in task_update.model_fields_set and task_update.title is not None and not task_update.title.strip()):
        raise HTTPException(status_code = status.HTTP_422_UNPROCESSABLE_ENTITY,detail = "Task titlee cannot be empty")

    return crud.update_task(db,task,task_update)



# delete a task

@app.delete("/tasks/{task_id}",status_code = status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int,db:Session = Depends(get_db)):

    task = crud.get_task(db,task_id)


    if task is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = "Task not foumd")

    crud.delete_task(db,task)
    return None



