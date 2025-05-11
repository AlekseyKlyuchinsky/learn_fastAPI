from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()


books = [
    {
        "id": 1,
        "title": "Асинхронность в Python",
        "author": "Мэттью",
    },
    {
        "id": 2,
        "title": "Backend разработка в Python",
        "author": "Артём",
    },
]


@app.get('/books', tags=['book'], summary='get all books')
def read_books():
    return books


@app.get('/books/{book_id}', tags=['book'], summary='get required book')
def get_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=404, detail='Book is not found')


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
