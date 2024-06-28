from fastapi import APIRouter

from app.api import models, service

books = APIRouter()


@books.post("/add_book", response_model=models.BookRspModel, status_code=200)
async def create_book(payload: models.CreateNewBookRqModel) -> models.BookRspModel:
    book_data = await service.create_book(payload=payload)
    return models.BookRspModel(**book_data)


@books.delete("/delete_book/{book_id}", response_model=models.EmptyModel, status_code=200)
async def delete_book(book_id: str) -> models.EmptyModel:
    await service.delete_book(book_id=book_id)
    return models.EmptyModel()


@books.get("/get_all_books", response_model=list[models.BookRspModel], status_code=200)
async def get_all_books() -> models.EmptyModel:
    all_books = await service.get_all_books()
    return [models.BookRspModel(**book_data) for book_data in all_books]


@books.put("/update_book", response_model=models.BookRspModel, status_code=200)
async def update_book(book_id: str, payload: models.UpdateBookRqModel) -> models.BookRspModel:
    updated_book_data = await service.update_book(book_id=book_id, update_data=payload)
    return models.BookRspModel(**updated_book_data)
