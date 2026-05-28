from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(DATABASE_URL)

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = "dbUsuarios"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)


Base.metadata.create_all(bind=engine)
