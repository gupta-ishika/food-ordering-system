from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_restaurant
from app.database.database import get_db
from app.models.category import Category
from app.models.food_item import FoodItem
from app.models.restaurant import Restaurant
from app.schemas.food_item import FoodItemCreate, FoodItemResponse

router = APIRouter(
    prefix="/food-items",
    tags=["Food Items"],
)


@router.post(
    "",
    response_model=FoodItemResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_food_item(
    food_item_data: FoodItemCreate,
    current_restaurant: Restaurant = Depends(get_current_restaurant),
    db: Session = Depends(get_db),
):
    category = (
        db.query(Category)
        .filter(
            Category.id == food_item_data.category_id,
            Category.restaurant_id == current_restaurant.id,
        )
        .first()
    )

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )

    new_food_item = FoodItem(
        category_id=food_item_data.category_id,
        name=food_item_data.name,
        description=food_item_data.description,
        price=food_item_data.price,
        image_url=food_item_data.image_url,
        is_available=food_item_data.is_available,
        is_veg=food_item_data.is_veg,
        display_order=food_item_data.display_order,
    )

    db.add(new_food_item)
    db.commit()
    db.refresh(new_food_item)

    return new_food_item