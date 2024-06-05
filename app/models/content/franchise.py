from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from ..base import Base

from ..mixins import (
    ContentMixin,
    UpdatedMixin,
)


class Franchise(Base, ContentMixin, UpdatedMixin):
    __tablename__ = "service_content_franchises"

    scored_by: Mapped[int] = mapped_column(default=0)
    score: Mapped[float] = mapped_column(default=0)

    anime: Mapped[list["Anime"]] = relationship(
        back_populates="franchise_relation"
    )

    manga: Mapped[list["Manga"]] = relationship(
        back_populates="franchise_relation"
    )
