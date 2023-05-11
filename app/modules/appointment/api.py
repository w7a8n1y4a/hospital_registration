from app.modules.appointment import crud
from app.modules.appointment.models import (AppointmentRead, AppointmentCreate)
from fastapi import APIRouter, Depends
from sqlmodel import Session
from starlette.status import HTTP_200_OK

from app.core.db import get_session

router = APIRouter()


@router.get("", response_model=AppointmentRead, status_code=HTTP_200_OK)
def get_appointment(
        appointment_id: int,
        session: Session = Depends(get_session)
):
    return crud.get(appointment_id, session)


@router.post("", response_model=AppointmentRead, status_code=HTTP_200_OK)
def create_appointment(
        data: AppointmentCreate,
        session: Session = Depends(get_session)
):
    return crud.create(data, session)
