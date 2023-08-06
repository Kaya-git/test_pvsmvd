from typing import TYPE_CHECKING
from .base import Base
from typing import List
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from .author_book import author_book_table

if TYPE_CHECKING:
    from .book import Book

class Author(Base):
    __tablename__ = "author"
    
    id: Mapped[int]= mapped_column(
        sa.Integer,
        autoincrement=True,
        primary_key=True
    )
    name: Mapped[str] = mapped_column(
        sa.Text,
        unique=False,
        nullable=False,
    )
    second_name: Mapped[str] = mapped_column(
        sa.Text,
        unique=False,
        nullable=False,
    )
    last_name: Mapped[str] = mapped_column(
        sa.Text,
        unique=False,
        nullable=False,
    )
    date_of_birth: Mapped[datetime] = mapped_column(
        sa.Date,
        unique=False,
        nullable=False,
    )
    books: Mapped[List["Book"]] = relationship(
        secondary=author_book_table,
        back_populates="authors",
    )
