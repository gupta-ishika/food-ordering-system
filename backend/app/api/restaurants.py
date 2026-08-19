from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_restaurant
from app.database.database import get_db
from app.models.restaurant import Restaurant
from app.schemas.restaurant import RestaurantResponse, RestaurantUpdate

router = APIRouter(
    prefix="/restaurants",
    tags=["Restaurants"],
)


@router.get("/me", response_model=RestaurantResponse)
def get_my_restaurant(
    current_restaurant: Restaurant = Depends(get_current_restaurant),
):
    return current_restaurant


@router.put("/me", response_model=RestaurantResponse)
def update_my_restaurant(
    restaurant_data: RestaurantUpdate,
    current_restaurant: Restaurant = Depends(get_current_restaurant),
    db: Session = Depends(get_db),
):
    current_restaurant.name = restaurant_data.name
    current_restaurant.address = restaurant_data.address
    current_restaurant.phone = restaurant_data.phone
    current_restaurant.logo_url = restaurant_data.logo_url

    db.commit()
    db.refresh(current_restaurant)

    return current_restaurant