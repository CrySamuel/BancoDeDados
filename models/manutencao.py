from sqlalchemy import Column, Integer, String, ForeignKey
from models import Base

class Manutencao(Base):
    __tablename__ = "manutencao"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    nome = Column(String(100), nullable=False)
    setor = Column(String(50), nullable=False)
