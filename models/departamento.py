from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models import Base  

class Departamento(Base):
    __tablename__ = "departamento" 

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = Column(String(50), nullable=False)
    genero = Column(String(50), nullable=False)

    funcionarios = relationship('Funcionario', back_populates='departamento')
