from fastapi import HTTPException

from app.api import db, db_manager, models


async def create_book(payload: models.CreateNewBookRqModel) -> dict:
    serial_number_exists: bool = await db_manager.check_if_serial_number_exists(serial_number=payload.serial_number)
    if serial_number_exists:
        raise HTTPException(status_code=404, detail="Serial Number already presented")
    book: db.Book = await db_manager.create_database_book_row(payload=payload)
    return {
        "id": str(book.id),
        "serial_number": book.serial_number,
        "title": book.title,
        "author": book.author,
        "is_borrowed": book.is_borrowed,
        "borrower_number": book.borrower_number,
        "borrowed_at": book.borrowed_at,
    }


async def delete_book(book_id: str) -> None:
    book_exists: bool = await db_manager.check_if_book_exists(book_id=book_id)
    if not book_exists:
        raise HTTPException(status_code=404, detail=f"Book: {book_id} does not exist.")
    await db_manager.delete_database_book_row(book_id=book_id)


async def get_all_books() -> list[dict]:
    books: list = await db_manager.get_all_books()
    return [
        {
            "id": str(book.id),
            "serial_number": book.serial_number,
            "title": book.title,
            "author": book.author,
            "is_borrowed": book.is_borrowed,
            "borrower_number": book.borrower_number,
            "borrowed_at": book.borrowed_at,
        }
        for book in books
    ]


async def update_book(book_id: str, update_data: models.UpdateBookRqModel) -> dict:
    book_exists: bool = await db_manager.check_if_book_exists(book_id=book_id)
    if not book_exists:
        raise HTTPException(status_code=404, detail=f"Book: {book_id} does not exist.")
    updated_book = await db_manager.update_database_book_row(book_id=book_id, update_data=update_data)
    return {
        "id": str(updated_book.id),
        "serial_number": updated_book.serial_number,
        "title": updated_book.title,
        "author": updated_book.author,
        "is_borrowed": updated_book.is_borrowed,
        "borrower_number": updated_book.borrower_number,
        "borrowed_at": updated_book.borrowed_at,
    }
