from fastapi import APIRouter
from database import create_session_maker, Author
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import Database as db
from datetime import datetime


author_router = APIRouter(
    prefix="/author",
    tags=["Author"]
)


@author_router.get("/{ident}")
async def get_author(
    ident: int | str,
):
    await db.author.get_by_id(
        ident=ident
    )


@author_router.get("")
async def get_all_authors():
    await db.author.get_all()


@author_router.post("")
async def new(
    name: str,
    second_name: str,
    last_name: str,
    date_of_birth: datetime, 
):
    await db.author.post(
        name=name,
        second_name=second_name,
        last_name=last_name,
        date_of_birth=date_of_birth
    )
    await db.session.commit()

@author_router.patch("")
async def update(
    ident: int,
    name: str,
    second_name: str,
    last_name: str,
    date_of_birth: datetime
):
    try:
        await db.author.patch(
            whereclause=(Author.id==ident),
            name=name,
            second_name=second_name,
            last_name=last_name,
            date_of_birth=date_of_birth
        )
        await db.session.commit()
    except:
        raise SyntaxError
    


@author_router.delete("")
async def delete(
    ident: int
):
    try:
        await db.author.delete(
            whereclause=(Author.id == ident)
        )
        await db.session.commit()
    except:
        raise SyntaxError
    