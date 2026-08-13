from pydantic import BaseModel, EmailStr


class RestaurantRegister(BaseModel):
    name: str
    email: EmailStr
    password: str
    address: str
    phone: str


class RestaurantLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str