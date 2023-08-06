"""Genre repository file."""
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update
from db.models import Genre, Book
from .abstract import Repository
from typing import List


class GenreRepo(Repository[Genre]):
    """Book repository for CRUD and other SQL queries."""

    def __init__(self, session: AsyncSession):
        """Initialize chat repository as for all chats or only for one chat."""
        super().__init__(type_model=Genre, session=session)

    async def post(
        self,
        name: str,
        books: List[Book] | Book,
    ) -> None:
        """
        Insert a new genre into the database.
        :param whereclause: Clause by which entry will be found
        :name: Genre name
        :books: List of books with certain genre
        """
        new_genre = await self.session.merge(
            Genre(
                name=name,
                books=books,
            )
        )
        return new_genre

    async def patch(
        self,
        whereclause,
        name: str,
        books: List[Book] | Book,
    ) -> None:
        """
        Update method for certain raw.
        :param whereclause: Clause by which entry will be found
        :name: Genre name
        :books: List of books with certain genre
        """
        statement = (
            update(self.type_model)
            .where(whereclause)
            .values(
                name=name,
                books=books,
            )
        )
        return (await self.session.execute(statement))
