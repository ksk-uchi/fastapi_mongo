from __future__ import annotations

import enum
from datetime import date, datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from ..types.pyobject_id import PyObjectId


class ToDoStatus(str, enum.Enum):
    ACTIVE: str = "active"
    DONE: str = "done"


class TodoItem(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    title: str
    description: str
    created_by: str
    until: date
    status: ToDoStatus = ToDoStatus.ACTIVE
    created_at: datetime
    updated_at: datetime

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
