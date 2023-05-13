from fastapi import Depends, HTTPException, status
from sqlmodel import Session
import random
from app.core.db import get_session
from app.modules.appointment import api_services
from app.modules.appointment.api_services import get_queue_info, register
from app.modules.appointment.models import Appointment, AppointmentCreate, OrganizationRead, AppointmentRead
from app.modules.user.models import User


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
) -> AppointmentRead:

    user = db.get(User, data.user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User is not found"
        )

    family, given, middle = [item for item in data.doctor_name.split(' ')]

    data = {
        'patient': {
            'birthdate': str(user.date_of_birth),
            'family': user.first_name,
            'given': user.second_name,
            'middle': user.patronymic,
            'sex': '2',
            'docnum_pfr': user.snils,
            'docnum_polis': str(random.randint(1000000000000000, 9999999999999999))
        },
        'referral': {
            'type': data.direction_type_code,  # тип направления - код
            'service': data.type_of_assistance,  # составной профиль помощи - вид помощи нужен код
            'id': '0',
            'target': data.target_organization
        },
        'doctor': {
            'family': family,
            'given': given,
            'middle': middle,
            'sex': '1',
            'id': '29',
            'docnum': '05513212414'
        }
    }


    try:
        key, code = register(data)
        return AppointmentRead(key=key, code=code)
    except:
        return AppointmentRead(key='0', code='0')

