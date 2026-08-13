from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.restaurant import Restaurant
from app.schemas.auth import RestaurantRegister, RestaurantLogin, Token
from app.core.security import hash_password, create_access_token, verify_password
from app.api.deps import get_current_restaurant

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
)
def register_restaurant(
    restaurant: RestaurantRegister,
    db: Session = Depends(get_db),
):
    existing_restaurant = (
        db.query(Restaurant)
        .filter(Restaurant.email == restaurant.email)
        .first()
    )

    if existing_restaurant:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    new_restaurant = Restaurant(
        name=restaurant.name,
        email=restaurant.email,
        hashed_password=hash_password(
            restaurant.password
        ),
        address=restaurant.address,
        phone=restaurant.phone,
    )

    db.add(new_restaurant)
    db.commit()
    db.refresh(new_restaurant)

    return {
        "message": "Restaurant registered successfully",
    }


@router.post("/login", response_model=Token)
def login_restaurant(
    restaurant: RestaurantLogin,
    db: Session = Depends(get_db),
):
    existing_restaurant = (
        db.query(Restaurant)
        .filter(Restaurant.email == restaurant.email)
        .first()
    )

    if not existing_restaurant:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    if not verify_password(
        restaurant.password,
        existing_restaurant.hashed_password,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    access_token = create_access_token(
        data={"sub": str(existing_restaurant.id)}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


@router.get("/me")
def get_me(
    current_restaurant: Restaurant = Depends(get_current_restaurant),
):
    return {
        "id": current_restaurant.id,
        "name": current_restaurant.name,
        "email": current_restaurant.email,
        "address": current_restaurant.address,
        "phone": current_restaurant.phone,
        "logo_url": current_restaurant.logo_url,
        "is_active": current_restaurant.is_active,
    }