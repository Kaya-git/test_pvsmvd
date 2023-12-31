from .base import Base
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from .book import Book


class Genre(Base):
    __tablename__ = "genre"

    id: Mapped[int] = mapped_column(
        sa.Integer,
        autoincrement=True,
        primary_key=True,
    )
    name: Mapped[str] = mapped_column(
        sa.Text,
        unique=False,
        nullable=False,
    )
    books: Mapped["Book"] = mapped_column(
        sa.ForeignKey("book.id"),
    )
