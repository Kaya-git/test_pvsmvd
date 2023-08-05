""" Repository file """
import abc
from typing import Generic, List, Type, TypeVar

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.base import Base

AbstractModel = TypeVar("AbstractModel")


class Repository(Generic[AbstractModel]):
    """Repository abstract class"""

    type_model: Type[Base]
    session: AsyncSession

    def __init__(self, type_model: Type[Base], session: AsyncSession):
        """
        Initialize abstract repository class
        :param type_model: Which model will be used for operations
        :param session: Session in which repository will work
        """
        self.type_model = type_model
        self.session = session


    async def get_by_id(self, ident: int | str) -> AbstractModel:
        """
        Get an ONE model from the database with PK
        :param ident: Key which need to find entry in database
        :return:
        """
        return await self.session.get(entity=self.type_model, ident=ident)


    async def get_all(self) -> AbstractModel:
        """
        Get all rows of the model from the database with whereclause
        :return:
        """
        statement = select(self.type_model)
        
        return self.session.scalars(statement)


    @abc.abstractmethod
    async def post(self, *args, **kwargs) -> None:
        """
        This method is need to be implemented in child classes,
        it is responsible for adding a new model to the database
        :return: Nothing
        """
        ...

    @abc.abstractclassmethod
    async def patch(self, *args, **kwargs) -> None:
        """
        This method is need to be implemented in child classes,
        it is responsible for updating row in a model
        :return: Nothing
        """
        ...


    async def delete(self, whereclause) -> None:
        """
        Delete model from the database

        :param whereclause: (Optional) Which statement
        :return: Nothing
        """
        statement = delete(self.type_model).where(whereclause)
        await self.session.execute(statement)
