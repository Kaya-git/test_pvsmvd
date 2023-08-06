from sqlalchemy import Table, Column, ForeignKey
from .base import Base

author_book_table = Table(
    "author_book",
    Base.metadata,
    Column("author_id", ForeignKey("author.id"), primary_key=True),
    Column("book_id", ForeignKey("book.id"), primary_key=True),
)
