"""Book repository file."""
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update
from database.models import Author, Book, PublishStatus
from .abstract import Repository
from typing import Optional, List
from datetime import datetime


class BookRepo(Repository[Author]):
    """Book repository for CRUD and other SQL queries."""

    def __init__(self, session: AsyncSession):
        """Initialize chat repository as for all chats or only for one chat."""
        super().__init__(type_model=Book, session=session)


    async def post(
        self,
        name: str,
        authors: Optional[List[Author] | Author],
        number_of_pages: int,
        published: PublishStatus,
    ) -> None:
        """
        Insert a new book into the database.
        :param whereclause: Clause by which entry will be found
        :name: Book name
        :authors: List of authors id or single author id
        :number_of_pages: Number of book pages
        :published: Status of publishing
        """
        new_book = await self.session.merge(
            Book(
                name=name,
                authors=authors,
                number_of_pages=number_of_pages,
                published=published,
            )
        )
        return new_book


    async def patch(
        self,
        whereclause,
        name: str,
        authors: Optional[List[Author] | Author],
        number_of_pages: int,
        published: PublishStatus,
    ) -> None:
        """
        Update method for certain raw.
        :param whereclause: Clause by which entry will be found
        :name: Book name
        :authors: List of authors id or single author id
        :number_of_pages: Number of book pages
        :published: Status of publishing
        """
        statement = (
            update(self.type_model)
            .where(whereclause)
            .values(
                name=name,
                authors=authors,
                number_of_pages=number_of_pages,
                published=published
            )
        )
        return (await self.session.execute(statement))
        