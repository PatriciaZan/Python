from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import get_db
from .models import User
from .schemas import LoginRequest, LoginResponse
from .security import verify_password, create_access_token


router = APIRouter()


@router.post("/login", response_model=LoginResponse)
def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(User.username == login_data.username)
        .first()
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    password_correct = verify_password(
        login_data.password,
        user.password_hash
    )

    if not password_correct:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    token = create_access_token(user.username)

    return LoginResponse(
        authenticated=True,
        userName=user.username,
        userPermission=user.user_permission,
        access_token=token
    )