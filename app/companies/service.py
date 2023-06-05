from app.models import Company, CompanyAnime, Anime
from sqlalchemy.ext.asyncio import AsyncSession
from app.service import anime_loadonly
from sqlalchemy.orm import joinedload
from sqlalchemy import select, desc
from sqlalchemy import func
from typing import Union


async def get_company_by_slug(
    session: AsyncSession, slug: str
) -> Union[Company, None]:
    return await session.scalar(select(Company).filter_by(slug=slug))


async def search_total(session: AsyncSession):
    return await session.scalar(select(func.count(Company.id)))


async def companies_search(
    session: AsyncSession,
    limit: int,
    offset: int,
):
    query = select(Company).order_by(desc("favorites"), desc("content_id"))
    query = query.limit(limit).offset(offset)
    return await session.scalars(query)


async def company_anime_total(
    session: AsyncSession, company: Company, company_type: Union[str, None]
):
    query = select(func.count(CompanyAnime.id)).filter_by(company=company)

    if company_type:
        query = query.filter_by(type=company_type)

    return await session.scalar(query)


async def company_anime(
    session: AsyncSession,
    company: Company,
    company_type: Union[str, None],
    limit: int,
    offset: int,
):
    query = select(CompanyAnime).filter_by(company=company)

    if company_type:
        query = query.filter_by(type=company_type)

    return await session.scalars(
        query.join(Anime)
        .options(anime_loadonly(joinedload(CompanyAnime.anime)))
        .order_by(
            desc(Anime.score), desc(Anime.scored_by), desc(Anime.content_id)
        )
        .limit(limit)
        .offset(offset)
    )