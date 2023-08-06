from pydantic import BaseModel
from datetime import datetime

class AuthorCreate(BaseModel):
    name: str
    second_name: str
    last_name: str
    date_of_birth: datetime
