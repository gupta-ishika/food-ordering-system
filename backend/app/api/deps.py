from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
# from jose import JWTError
from sqlalchemy.orm import Session

from app.core.security import decode_access_token
from app.database.database import get_db
from app.models.restaurant import Restaurant

security = HTTPBearer()

def get_current_restaurant(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
) -> Restaurant:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = decode_access_token(credentials.credentials)

    if not payload:
        raise credentials_exception

    restaurant_id = payload.get("sub")

    if restaurant_id is None:
        raise credentials_exception

    try:
        restaurant_id = int(restaurant_id)
    except (TypeError, ValueError):
        raise credentials_exception

    restaurant = (
        db.query(Restaurant)
        .filter(Restaurant.id == restaurant_id)
        .first()
    )

    if restaurant is None or not restaurant.is_active:
        raise credentials_exception

    return restaurant