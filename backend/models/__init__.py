# standard library imports
from datetime import datetime

# third party imports
from sqlalchemy import (Boolean, DateTime, Integer, String)
from sqlalchemy.orm import (Mapped, mapped_column)

# local application imports
from backend.extensions import database


class User(database.Model):
    """
    Model representing the 'users' table.
    """
    # set table name
    __tablename__ = "users"

    # fields
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, default=datetime.now
    )
    email: Mapped[str] = mapped_column(
        String(255), nullable=False, unique=True
    )
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    password: Mapped[str] = mapped_column(
        String(255), nullable=False
    )
