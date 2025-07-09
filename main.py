from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

tasks = []

class Task(BaseModel):
    id: Optional[int] = Field(default_factory=lambda: len(tasks) + 1)
    title: str
    description: Optional[str] = None
    completed: bool = Field(default=False)

@app.get("/")
def read_root():
    return FileResponse("static/index.html")

@app.get("/tasks", status_code=status.HTTP_200_OK)
def get_tasks():
    return tasks

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: Task):
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            task.title = updated_task.title
            task.description = updated_task.description
            task.completed = updated_task.completed
            return task
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found"
    )

@app.delete("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {"message": "Task deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found"
    )