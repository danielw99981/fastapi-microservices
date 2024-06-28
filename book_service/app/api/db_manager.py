from itertools import chain

from sqlalchemy.future import select

from app.api import db, models


async def create_database_book_row(payload: models.CreateNewBookRqModel) -> db.Book:
    async with db.async_session() as session:
        book = db.Book(
            serial_number=payload.serial_number,
            title=payload.title,
            author=payload.author,
        )
        session.add(book)
        await session.commit()
        await session.refresh(book)
        return book


async def check_if_serial_number_exists(serial_number: int) -> bool:
    async with db.async_session() as session:
        book_serial_number_query = await session.scalars(
            select(db.Book.id).filter(db.Book.serial_number == serial_number)
        )
        book_id = book_serial_number_query.first()
        return bool(book_id)


async def check_if_book_exists(book_id: str) -> bool:
    async with db.async_session() as session:
        book_id_query = await session.scalars(select(db.Book.id).filter(db.Book.id == book_id))
        book_id = book_id_query.first()
        return bool(book_id)


async def delete_database_book_row(book_id: str) -> None:
    async with db.async_session() as session:
        book = await session.get(db.Book, book_id)
        await session.delete(book)
        await session.commit()


async def get_all_books() -> list[db.Book]:
    async with db.async_session() as session:
        books = await session.execute(select(db.Book))
        return chain.from_iterable(books.all())


async def update_database_book_row(book_id: str, update_data: models.UpdateBookRqModel) -> db.Book:
    async with db.async_session() as session:
        book = await session.get(db.Book, book_id)
        for key, new_value in update_data.model_dump(exclude_unset=True).items():
            if getattr(book, key) != new_value:
                setattr(book, key, new_value)
        await session.commit()
        await session.refresh(book)
        return book
