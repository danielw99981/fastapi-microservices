import uuid

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import (AsyncAttrs, AsyncSession,
                                    create_async_engine)
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.api import settings


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid1)
    serial_number = Column(Integer(), unique=True, nullable=False)
    title = Column(String(64), nullable=False)
    author = Column(String(64), nullable=False)
    is_borrowed = Column(Boolean(), nullable=False, default=False)
    borrower_number = Column(Integer(), nullable=True)
    borrowed_at = Column(DateTime(timezone=True), nullable=True)


engine = create_async_engine(settings.Config().postgresql_url, future=True, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
