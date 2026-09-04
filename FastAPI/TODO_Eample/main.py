from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal
from pathlib import Path
import json


app = FastAPI(title="TODO API")


# Location of our data file
DATA_FILE = Path(__file__).resolve().parent / "tasks.json"


# Model for creating a task
class TaskCreate(BaseModel):
    title: str
    description: str = ""


# Model for updating task status
class TaskUpdate(BaseModel):
    status: Literal[
        "not yet started",
        "in progress",
        "completed"
    ]


# Read tasks from the JSON file
def load_tasks():
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


# Save tasks to the JSON file
def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


# CREATE a task
@app.post("/tasks")
def create_task(task: TaskCreate):

    tasks = load_tasks()

    new_id = max(
        (item["id"] for item in tasks),
        default=0
    ) + 1

    new_task = {
        "id": new_id,
        "title": task.title,
        "description": task.description,
        "status": "not yet started"
    }

    tasks.append(new_task)

    save_tasks(tasks)

    return {
        "message": "Task created successfully",
        "task": new_task
    }


# READ all tasks
@app.get("/tasks")
def get_all_tasks():

    tasks = load_tasks()

    return {
        "total_tasks": len(tasks),
        "tasks": tasks
    }


# UPDATE task status
@app.put("/tasks/{task_id}")
def update_task_status(
    task_id: int,
    task: TaskUpdate
):

    tasks = load_tasks()

    for item in tasks:

        if item["id"] == task_id:

            item["status"] = task.status

            save_tasks(tasks)

            return {
                "message": "Task status updated successfully",
                "task": item
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


# DELETE a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    tasks = load_tasks()

    for item in tasks:

        if item["id"] == task_id:

            tasks.remove(item)

            save_tasks(tasks)

            return {
                "message": "Task deleted successfully",
                "deleted_task": item
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )