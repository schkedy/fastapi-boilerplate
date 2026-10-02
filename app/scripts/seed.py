"""
Идемпотентное заполнение БД тестовыми пользователями.
Запуск: python -m scripts.seed
"""
import asyncio
import os

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

# Подставьте свои импорты
from app.models.user import User
from app.core.security import hash_password
from app.core.config import settings

DATABASE_URL = settings.database_url

SEED_USERS = [
    {"name": "Admin",    "email": "admin@example.com",    "password": "admin123",    "is_active": True},
    {"name": "Test User","email": "user@example.com",     "password": "user123",     "is_active": True},
    {"name": "Inactive", "email": "inactive@example.com", "password": "inactive123", "is_active": False},
]


async def seed() -> None:
    engine = create_async_engine(DATABASE_URL, echo=False)
    Session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with Session() as session:
        for data in SEED_USERS:
            exists = await session.scalar(
                select(User).where(User.email == data["email"])
            )
            if exists:
                print(f"⏭  skip: {data['email']} (уже есть)")
                continue

            user = User(
                name=data["name"],
                email=data["email"],
                hashed_password=hash_password(data["password"]),
                is_active=data["is_active"],
            )
            session.add(user)
            print(f"✅ created: {data['email']}")

        await session.commit()

    await engine.dispose()
    print("🌱 seed завершён")


if __name__ == "__main__":
    asyncio.run(seed())