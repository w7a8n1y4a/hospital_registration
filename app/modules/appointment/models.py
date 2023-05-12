from datetime import date

from pydantic import BaseModel
from sqlmodel import SQLModel, Field

from app.modules.appointment.examples import ex_appointment_read, \
    ex_appointment_create


class AppointmentBase(SQLModel):
    id: int = Field(primary_key=True)
    service_type: str = Field(max_length=255, nullable=False)
    doctor_name: str = Field(max_length=255, nullable=False)
    diagnosis_comment: str = Field(max_length=255, nullable=False)
    date_of_diagnosis: date = Field(nullable=False)
    id_diagnosis_status: int = Field(nullable=False)
    disease_code: str = Field(max_length=60, nullable=False)


class Appointment(AppointmentBase, table=True):
    __tablename__ = "appointments"


class AppointmentRead(AppointmentBase):
    class Config:
        schema_extra = {"example": ex_appointment_read}


class AppointmentCreate(BaseModel):
    service_type: str
    doctor_name: str
    diagnosis_comment: str
    date_of_diagnosis: date
    id_diagnosis_status: int
    disease_code: str

    class Config:
        use_enum_values = True
        schema_extra = {"example": ex_appointment_create}
