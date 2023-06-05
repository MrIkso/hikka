from app.sync.aggregator.info import update_anime_info
from app.service import get_user_by_username
from sqlalchemy.orm import selectinload
from app.database import sessionmanager
from sqlalchemy import select, desc
from datetime import datetime
from app.models import Anime
import asyncio
import config


async def test():
    sessionmanager.init(config.database)
    semaphore = asyncio.Semaphore(10)

    async with sessionmanager.session() as session:
        anime = await session.scalar(
            select(Anime).order_by(desc("score"), desc("scored_by")).limit(1)
        )

        await update_anime_info(semaphore, anime.content_id)


if __name__ == "__main__":
    asyncio.run(test())