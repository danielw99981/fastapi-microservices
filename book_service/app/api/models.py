from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class EmptyModel(BaseModel):
    pass


class CreateNewBookRqModel(BaseModel):
    serial_number: int = Field(ge=100000, le=999999)
    title: str = Field(min_length=1, max_length=64)
    author: str = Field(min_length=1, max_length=64)


class BookRspModel(CreateNewBookRqModel):
    id: str
    is_borrowed: bool | None
    borrower_number: int | None
    borrowed_at: datetime | None


class UpdateBookRqModel(BaseModel):
    is_borrowed: bool
    borrower_number: Optional[int] = Field(ge=100000, le=999999)
    borrowed_at: Optional[datetime]
