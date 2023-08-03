from fastapi import FastAPI
from config import conf
from database import create_async_engine

app = FastAPI(
    title="PVSMD Test")


engine = create_async_engine(conf.db.build_conn_str())


if __name__ =="__main__":
    import uvicorn
    
    
    uvicorn.run("main.py", log_level=conf.logging_level)
