from pydantic import BaseModel
from sqlmodel import SQLModel, Field

from app.modules.users.examples import ex_user_read, ex_user_create


class UserBase(SQLModel):
    id: int = Field(primary_key=True)
    name: str = Field(max_length=255, nullable=False)


class User(UserBase, table=True):
    __tablename__ = "users"


class UserRead(UserBase):
    class Config:
        schema_extra = {"example": ex_user_read}


class UserCreate(BaseModel):
    name: str

    class Config:
        use_enum_values = True
        schema_extra = {"example": ex_user_create}
