from app.schemas import AnimeFavouriteResponse, SuccessResponse
from app.models import User, Anime, AnimeFavourite
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from app.database import get_session
from typing import Tuple
from . import service

from .dependencies import (
    get_anime_favourite,
    add_anime_favourite,
)


# ToDo: Better responses
router = APIRouter(prefix="/favourite", tags=["Favourite"])


@router.get("/anime/{slug}", response_model=AnimeFavouriteResponse)
async def anime_favourite(
    favourite: AnimeFavourite = Depends(get_anime_favourite),
):
    return favourite


@router.put("/anime/{slug}", response_model=AnimeFavouriteResponse)
async def anime_favourite_add(
    data: Tuple[Anime, User] = Depends(add_anime_favourite),
    session: AsyncSession = Depends(get_session),
):
    return await service.create_anime_favourite(session, *data)


@router.delete("/anime/{slug}", response_model=SuccessResponse)
async def anime_favourite_delete(
    favourite: AnimeFavourite = Depends(get_anime_favourite),
    session: AsyncSession = Depends(get_session),
):
    await service.delete_anime_favourite(session, favourite)
    return {"success": True}
