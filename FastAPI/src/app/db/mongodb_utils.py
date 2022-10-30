from __future__ import annotations

import os
from logging import getLogger

from pymongo import MongoClient
from .mongodb import db


logger = getLogger("uvicorn")


def connect_mongo() -> MongoClient:
    logger.info("CREATE CONNECTION!!!")
    db.client = MongoClient(
        "mongo",
        27017,
        username=os.environ["MONGO_USER"],
        password=os.environ["MONGO_PASSWORD"]
    )


def close_mongo() -> None:
    db.client.close()
    logger.info("CLOSING CONNECTION!!!")

