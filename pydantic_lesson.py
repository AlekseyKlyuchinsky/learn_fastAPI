import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

data = {
    'email': 'abc@mail.ru',
    'bio': None,
    'age': 14,
}

users = []


class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=1000)
    age: int = Field(ge=0, le=140)


@app.post('/users')
def add_user(user: UserSchema):
    users.append(user)
    return {'ok': True, 'msg': 'User added'}


@app.get('/users')
def get_users():
    return users


if __name__ == '__main__':
    uvicorn.run('pydantic_lesson:app')
