from datetime import datetime

from pydantic import BaseModel, EmailStr


class RestaurantResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    address: str
    phone: str
    logo_url: str | None
    is_active: bool
    created_at: datetime
    updated_at: datetime

class RestaurantUpdate(BaseModel):
    name: str
    address: str
    phone: str
    logo_url: str | None = None

    model_config = {
        "from_attributes": True
    }