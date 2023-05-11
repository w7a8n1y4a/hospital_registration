from fastapi import APIRouter, Depends
from sqlmodel import Session
from starlette.status import HTTP_200_OK

from app.core.db import get_session
from app.modules.users import crud
from app.modules.users.models import UserRead, UserCreate

router = APIRouter()


@router.post("", response_model=UserRead, status_code=HTTP_200_OK)
def create_user(
        data: UserCreate,
        session: Session = Depends(get_session)
):
    return crud.create(data, session)
