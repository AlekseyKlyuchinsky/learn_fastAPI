from fastapi import FastAPI
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


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
