from fastapi import Depends, HTTPException, status
from sqlmodel import Session

from app.core.db import get_session
from app.modules.appointment import api_services
from app.modules.appointment.api_services import get_queue_info
from app.modules.appointment.models import Appointment, AppointmentCreate, OrganizationRead


def get(
        code: int,
        db: Session = Depends(get_session)
) -> list[OrganizationRead]:

    orgs_list = get_queue_info(code)

    if orgs_list == None:
        return []

    orgs_list_with_type = []
    for orgs in orgs_list:
        if orgs['address'] == None:
            orgs['address'] = 'Нет адреса'
        orgs_list_with_type.append(OrganizationRead(address=orgs['address'], code=orgs['code']))

    if len(orgs_list_with_type) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organization is not found"
        )

    return orgs_list_with_type


def create(
        data: AppointmentCreate,
        db: Session = Depends(get_session)
) -> Appointment:
    values = data.dict()

    appointment = Appointment(**values)
    db.add(appointment)

    # todo: add api call
    api_services.create_appointment(appointment)

    db.commit()
    db.refresh(appointment)

    return appointment
