from fastapi import FastAPI
from config import conf
from author import author_router

app = FastAPI(
    title="PVSMD Test")

app.include_router(author_router)


if __name__ =="__main__":
    import uvicorn
    
    
    uvicorn.run("main.py", log_level=conf.logging_level)
