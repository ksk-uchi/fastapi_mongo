from __future__ import annotations

from pymongo import MongoClient


class MyDB:
    client: MongoClient = None


db = MyDB


def get_cli() -> MongoClient:
    return db.client
