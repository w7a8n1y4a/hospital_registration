from fastapi import Depends, HTTPException, status
from sqlmodel import Session

from app.core.db import get_session
from app.modules.users.models import User, UserCreate, UserUpdate


def get(
        user_id: int,
        db: Session = Depends(get_session)
) -> User:
    user = db.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User is not found"
        )

    return user


def create(
        data: UserCreate,
        db: Session = Depends(get_session)
) -> User:
    values = data.dict()
    user = User(**values)
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def update(
        data: UserUpdate,
        db: Session = Depends(get_session)
) -> User:
    user = db.get(User, data.id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User is not found"
        )

    values = data.dict(exclude_unset=True)

    for k, v in values.items():
        setattr(user, k, v)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def delete(
        user_id: int,
        db: Session = Depends(get_session)
) -> bool:
    user = db.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User is not found"
        )
    db.delete(user)
    db.commit()

    return True
