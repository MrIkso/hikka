from sqlalchemy import ForeignKey, UniqueConstraint, String
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from ..base import Base


class AnimeStaff(Base):
    __tablename__ = "service_content_anime_staff"

    # ToDo: Roles model
    # roles: Mapped[list] = mapped_column(JSONB, default=[])
    # role: Mapped[str]

    person_id = mapped_column(
        ForeignKey("service_content_people.id"),
        index=True,
    )

    anime_id = mapped_column(
        ForeignKey("service_content_anime.id"),
        index=True,
    )

    person: Mapped["Person"] = relationship(
        back_populates="staff_roles", foreign_keys=[person_id]
    )

    anime: Mapped["Anime"] = relationship(
        back_populates="staff", foreign_keys=[anime_id]
    )

    unique_constraint = UniqueConstraint(person_id, anime_id)


class AnimeVoice(Base):
    __tablename__ = "service_content_anime_voices"

    language: Mapped[str] = mapped_column(String(32), index=True)

    character_id = mapped_column(
        ForeignKey("service_content_characters.id"),
        index=True,
    )

    person_id = mapped_column(
        ForeignKey("service_content_people.id"),
        index=True,
    )

    anime_id = mapped_column(
        ForeignKey("service_content_anime.id"),
        index=True,
    )

    character: Mapped["Character"] = relationship(
        back_populates="voices", foreign_keys=[character_id]
    )

    person: Mapped["Person"] = relationship(
        back_populates="voice_roles", foreign_keys=[person_id]
    )

    anime: Mapped["Anime"] = relationship(
        back_populates="voices", foreign_keys=[anime_id]
    )

    unique_constraint = UniqueConstraint(character_id, person_id, anime_id)
