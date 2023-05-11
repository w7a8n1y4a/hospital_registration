from datetime import datetime
from enum import Enum

from pydantic import BaseModel
from sqlalchemy import event, Column
from sqlalchemy.databases import postgres
from sqlmodel import SQLModel, Field

from app.modules.user.examples import ex_user_read, ex_user_create

genders = postgres.ENUM("MALE", "FEMALE", name="genders")


@event.listens_for(SQLModel.metadata, "before_create")
def _create_enums(metadata, conn, **kw):  # noqa: indirect usage
    genders.create(conn, checkfirst=True)


class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


class UserBase(SQLModel):
    id: int = Field(primary_key=True)
    first_name: str = Field(max_length=255, nullable=False)
    second_name: str = Field(max_length=255, nullable=False)
    patronymic: str = Field(max_length=255, nullable=False)
    date_of_birth: datetime = Field(nullable=False)
    gender: str = Field(sa_column=Column("gender", genders, nullable=False))


class User(UserBase, table=True):
    __tablename__ = "users"


class UserRead(UserBase):
    class Config:
        schema_extra = {"example": ex_user_read}


class UserCreate(BaseModel):
    first_name: str
    second_name: str
    patronymic: str
    date_of_birth: datetime
    gender: str

    class Config:
        use_enum_values = True
        schema_extra = {"example": ex_user_create}


class UserUpdate(UserBase):
    class Config:
        use_enum_values = True
        schema_extra = {"example": ex_user_read}
