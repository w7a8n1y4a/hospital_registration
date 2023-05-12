from fastapi import APIRouter, Depends
from sqlmodel import Session
from starlette.status import HTTP_200_OK

from app.core.db import get_session
from app.modules.user import crud
from app.modules.user.models import UserRead, UserCreate, UserUpdate

router = APIRouter()


@router.get("", response_model=UserRead, status_code=HTTP_200_OK)
def get_user(
        user_id: int,
        session: Session = Depends(get_session)
):
    return crud.get(user_id, session)


@router.post("", response_model=UserRead, status_code=HTTP_200_OK)
def create_user(
        data: UserCreate,
        session: Session = Depends(get_session)
):
    return crud.create(data, session)


@router.patch("", response_model=UserRead, status_code=HTTP_200_OK)
def update_user(
        data: UserUpdate,
        session: Session = Depends(get_session)
):
    return crud.update(data, session)


@router.delete("", response_model=bool, status_code=HTTP_200_OK)
def delete_user(
        user_id: int,
        session: Session = Depends(get_session)
):
    return crud.delete(user_id, session)


@router.get("/all", response_model=list[UserRead], status_code=HTTP_200_OK)
def get_users(
        session: Session = Depends(get_session)
):
    return crud.get_all(session)
