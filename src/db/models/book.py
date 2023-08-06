from typing import TYPE_CHECKING
from .base import Base
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
import enum
from .author_book import author_book_table

if TYPE_CHECKING:
    from .author import Author



class PublishStatus(enum.IntEnum):
    No = 0
    Yes = 1


class Book(Base):
    __tablename__ = "book"
    
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
    authors: Mapped[List["Author"] | "Author"] = relationship(
        secondary=author_book_table,
        back_populates="books",
    )
    number_of_pages: Mapped[int] = mapped_column(
        sa.Integer,
        unique=False,
        nullable=False,
    )
    published: Mapped[PublishStatus] = mapped_column(
        sa.Enum(PublishStatus),
    )
