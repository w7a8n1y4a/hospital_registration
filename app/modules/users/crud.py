from fastapi import Depends
from sqlmodel import Session

from app.core.db import get_session
from app.modules.users.models import User, UserCreate


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
