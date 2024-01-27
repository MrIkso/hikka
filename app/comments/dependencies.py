from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies import auth_required
from app.models import Comment, Edit, User
from app.database import get_session
from .utils import is_empty_markdown
from app.errors import Abort
from fastapi import Depends
from app import constants
from . import service

from .schemas import (
    ContentTypeEnum,
    CommentArgs,
)


async def validate_content(
    slug: str,
    content_type: ContentTypeEnum,
    session: AsyncSession = Depends(get_session),
) -> Edit:
    if not (
        content := await service.get_content_by_slug(
            session, content_type, slug
        )
    ):
        raise Abort("comment", "content-not-found")

    return content


async def validate_content_slug(
    content: Edit = Depends(validate_content),
) -> str:
    return content.reference


async def validate_parent(
    args: CommentArgs,
    content_type: ContentTypeEnum,
    content_id: Edit = Depends(validate_content_slug),
    session: AsyncSession = Depends(get_session),
) -> Comment | None:
    if not args.parent:
        return None

    if not (
        parent_comment := await service.get_comment(
            session, content_type, content_id, args.parent
        )
    ):
        raise Abort("comment", "parent-not-found")

    max_reply_depth = 3
    if len(parent_comment.path) > max_reply_depth:
        raise Abort("comment", "max-depth")

    return parent_comment


async def validate_rate_limit(
    session: AsyncSession = Depends(get_session),
    author: User = Depends(
        auth_required(permissions=[constants.PERMISSION_WRITE_COMMENT])
    ),
):
    comments_limit = 100
    comments_total = await service.count_comments_limit(session, author)

    if comments_total >= comments_limit:
        raise Abort("comment", "rate-limit")

    return author


async def validate_comment_args(args: CommentArgs):
    if is_empty_markdown(args.text):
        raise Abort("comment", "empty-markdown")

    return args