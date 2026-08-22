from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.restaurant import Restaurant
from app.models.table import Table

router = APIRouter(prefix="/public", tags=["Public"])


@router.get("/tables/{table_id}")
def get_public_table(table_id: int, db: Session = Depends(get_db)):
    result = (
        db.query(Table, Restaurant)
        .join(Restaurant, Table.restaurant_id == Restaurant.id)
        .filter(
            Table.id == table_id,
            Table.is_active == True,
            Restaurant.is_active == True,
        )
        .first()
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Table not found",
        )

    table, restaurant = result

    return {
        "table_id": table.id,
        "table_number": table.table_number,
        "restaurant_id": restaurant.id,
        "restaurant_name": restaurant.name,
    }