import os
from dotenv import load_dotenv
from sqlalchemy.engine import URL
from dataclasses import dataclass


load_dotenv()


@dataclass
class DatabaseConfig:
    database_system: str = "sqlite"
    driver: str = "aiosqlite"
    def build_conn_str(self) -> str:
        return URL.create(
            drivername=f"{self.database_system}+{self.driver}",
        ).render_as_string()

@dataclass
class Configuration:
    debug = bool(os.environ.get("DEBUG"))
    logging_level = int(os.environ.get("LOGGING_LEVEL"))
    
    db = DatabaseConfig()

conf = Configuration()
