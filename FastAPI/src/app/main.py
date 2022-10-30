from __future__ import annotations

from logging import INFO, getLogger

from bson.objectid import ObjectId
from fastapi import FastAPI

from .db.mongodb_utils import close_mongo, connect_mongo
from .db.mongodb import get_cli

from .models.todo_item import TodoItem


app = FastAPI()
app.add_event_handler("startup", connect_mongo)
app.add_event_handler("shutdown", close_mongo)

logger = getLogger("uvicorn")


@app.get("/")
def read_root() -> dict:
    return {"Hello": "World!!"}


@app.get("/items")
def list_items() -> list:
    cli = get_cli()
    todo_items = cli.mydb.todo_items
    items = [TodoItem(**item) for item in todo_items.find()]
    return items


@app.get("/items/{item_id}")
def read_item(item_id: str) -> dict:
    cli = get_cli()
    item = cli.mydb.todo_items.find_one({"_id": ObjectId(item_id)})
    return TodoItem(**item)
