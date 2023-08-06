"""Author repository file."""
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update
from db.models import Author, Book
from .abstract import Repository
from typing import Optional, List
from datetime import datetime


class AuthorRepo(Repository[Author]):
    """Author repository for CRUD and other SQL queries."""

    def __init__(self, session: AsyncSession):
        """Initialize chat repository as for all chats or only for one chat."""
        super().__init__(type_model=Author, session=session)

    async def post(
        self,
        name: str,
        second_name: str,
        last_name: str,
        date_of_birth: datetime,
        books: Optional[List[Book]] | Book,
    ) -> None:
        """
        Insert a new author into the database.
        :param whereclause: Clause by which entry will be found
        :name: Author name
        :second_name: Author second name
        :last_name: Author last name
        :date_of_birth: Author date of birth
        :books: Author book or books
        """
        new_author = await self.session.merge(
            Author(
                name=name,
                second_name=second_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
            )
        )
        return new_author

    async def patch(
        self,
        whereclause,
        name: str,
        second_name: str,
        last_name: str,
        date_of_birth: datetime,
    ) -> None:
        """
        Update method for certain raw.
        :param whereclause: Clause by which entry will be found
        :name: Author name
        :second_name: Author second name
        :last_name: Author last name
        :date_of_birth: Author date of birth
        """
        statement = (
            update(self.type_model)
            .where(whereclause)
            .values(
                name=name,
                second_name=second_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                )
        )
        return (await self.session.execute(statement))
        