from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import Message, UserSchema

app = FastAPI()


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Hello World"}


@app.post("/users/")
def create_user(user: UserSchema):
    pass
