from fastapi import Depends, HTTPException, status
from sqlmodel import Session

from app.core.db import get_session
from app.modules.appointment.models import Appointment, AppointmentCreate


def get(
        user_id: int,
        db: Session = Depends(get_session)
) -> Appointment:
    appointment = db.get(Appointment, user_id)

    if not appointment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appointment is not found"
        )

    return appointment


def create(
        data: AppointmentCreate,
        db: Session = Depends(get_session)
) -> Appointment:
    values = data.dict()
    appointment = Appointment(**values)
    db.add(appointment)
    db.commit()
    db.refresh(appointment)

    return appointment
