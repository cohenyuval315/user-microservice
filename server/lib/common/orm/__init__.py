from .database import Database
import os


# SQLALCHEMY_DATABASE_URL = os.environ.get("SQLALCHEMY_DATABASE_URL","sqlite+pysqlite:///:memory:")
SQLALCHEMY_DATABASE_URL = os.environ.get("SQLALCHEMY_DATABASE_URL","postgresql+asyncpg://myuser:mypassword@localhost:5432/mydatabase")
db = Database() 
db.initialize(sqlalchemy_database_url=SQLALCHEMY_DATABASE_URL)


async def hello():
    await db.get_session_factory().create_session().add()