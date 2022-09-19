from __future__ import annotations

import os

from bson.objectid import ObjectId
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

def _get_mydb():
    cli = MongoClient("mongo", 27017, username=os.environ["MONGO_USER"], password=os.environ["MONGO_PASSWORD"])
    return cli.mydb


@app.get("/")
def read_root() -> dict:
    return {"Hello": "World!!"}


@app.get("/items")
def list_items() -> list:
    mydb = _get_mydb()
    todo_items = mydb.todo_items
    items = [{**item, "_id": str(item["_id"])} for item in todo_items.find()]
    return items


@app.get("/items/{item_id}")
def read_item(item_id: str) -> dict:
    mydb = _get_mydb()
    item = mydb.todo_items.find({"_id": ObjectId(item_id)})
    return [{**i, "_id": str(i["_id"])} for i in item]
