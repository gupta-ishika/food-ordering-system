from datetime import datetime

from pydantic import BaseModel


class TableCreate(BaseModel):
    table_number: str
    qr_code_url: str


class TableResponse(BaseModel):
    id: int
    restaurant_id: int
    table_number: str
    qr_code_url: str
    is_active: bool

    model_config = {
        "from_attributes": True
    }