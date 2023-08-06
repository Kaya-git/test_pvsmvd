from fastapi import APIRouter
from db import Author
from database import Database as db
from datetime import datetime


author_router = APIRouter(
    prefix="/author",
    tags=["Author"]
)


@author_router.get("/{id}")
async def get_author(
    id: int | str,
):
    await db.author.get_by_id(
        id==id
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
        await db.author.patch(
            whereclause=(Author.id==ident),
            name=name,
            second_name=second_name,
            last_name=last_name,
            date_of_birth=date_of_birth
        )
        await db.session.commit()


@author_router.delete("")
async def delete(
    ident: int
):
        await db.author.delete(
            whereclause=(Author.id == ident)
        )
        await db.session.commit()
    