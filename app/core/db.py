from fastapi.encoders import jsonable_encoder
from sqlmodel import Session, create_engine

from app import settings

engine = create_engine(
    settings.database_url,
    echo=True,
    future=True,
    json_serializer=jsonable_encoder,
    pool_pre_ping=True
)


def get_session() -> Session:
    with Session(engine) as session:
        yield session

# async_engine = create_async_engine(
#     settings.database_url,
#     echo=True,
#     future=True,
#     pool_pre_ping=True
# )
#
#
# async def get_async_session() -> AsyncSession:
#     async_session = sessionmaker(
#         bind=async_engine, class_=AsyncSession, expire_on_commit=False
#     )
#     async with async_session() as session:
#         yield session
