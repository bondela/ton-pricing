from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from config import DATABASE_STRING
from database.models import Base

engine = create_async_engine(DATABASE_STRING)
database_session = async_sessionmaker(engine)


async def run_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
