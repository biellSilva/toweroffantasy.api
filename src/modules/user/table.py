from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from src._settings import config
from src._utils import current_datetime
from src.modules.base.table import BaseTable


class UserTable(BaseTable):
    """UserTable model."""

    __tablename__ = "db_users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, sort_order=-1)
    created_at: Mapped[datetime] = mapped_column(
        __type_pos=DateTime(timezone=True),
        default=current_datetime,
        sort_order=-1,
    )
    updated_at: Mapped[datetime] = mapped_column(
        __type_pos=DateTime(timezone=True),
        default=current_datetime,
        onupdate=current_datetime,
        sort_order=-1,
    )

    username: Mapped[str] = mapped_column(
        __type_pos=String(config.USERNAME_MAX_LENGTH),
        unique=True,
    )
    email: Mapped[str] = mapped_column(
        __type_pos=String(config.EMAIL_MAX_LENGTH),
        unique=True,
    )
    password: Mapped[str]

    def __repr__(self) -> str:
        """Return a string representation of the model."""
        return f"< UserTable id={self.id} username={self.username} email={self.email} >"
