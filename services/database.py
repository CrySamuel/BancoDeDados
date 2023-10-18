from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from urllib.parse import quote

instance = f"mysql+pymysql://root:{quote('2810leticia')}@localhost:3306/loja2"

if not database_exists(instance):
    create_database(instance)

engine = create_engine(instance, echo=True)
session = Session(bind=engine, autocommit=False, autoflush=True)
