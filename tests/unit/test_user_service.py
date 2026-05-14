from unittest.mock import AsyncMock, MagicMock

import pytest

from app.schemas.user import UserCreate
from app.services.user_service import UserService


@pytest.mark.asyncio
async def test_create_user_success():
    mock_repo = MagicMock()
    mock_repo.get_by_email = AsyncMock(return_value=None)
    mock_repo.create = AsyncMock(
        return_value=MagicMock(id=1, name="Julio", email="julio@example.com", is_active=True)
    )

    service = UserService(mock_repo)
    data = UserCreate(name="Julio", email="julio@example.com", password="secret123")

    user = await service.create_user(data)

    assert user.email == "julio@example.com"
    mock_repo.create.assert_called_once()


@pytest.mark.asyncio
async def test_create_user_duplicate_email():
    from fastapi import HTTPException

    mock_repo = MagicMock()
    mock_repo.get_by_email = AsyncMock(return_value=MagicMock())

    service = UserService(mock_repo)
    data = UserCreate(name="Julio", email="julio@example.com", password="secret123")

    with pytest.raises(HTTPException) as exc_info:
        await service.create_user(data)

    assert exc_info.value.status_code == 409
