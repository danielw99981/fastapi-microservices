from fastapi import FastAPI

from app.api.db import Base, engine
from app.api.routes import books

app = FastAPI(openapi_url="/api/v1/books/openapi.json", docs_url="/api/v1/books/docs")


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(books, prefix="/api/v1/books", tags=["accounts"])
