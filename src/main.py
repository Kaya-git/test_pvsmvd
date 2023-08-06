from fastapi import FastAPI
from config import conf
from author import author_router

app = FastAPI(
    title="PVSMD Test")

app.include_router(author_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True, log_level=conf.logging_level)
