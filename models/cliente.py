from sqlalchemy import Column, Integer, String, CHAR, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.base import Base


class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = Column(String(100), nullable=False)
    cpf = Column(CHAR(11), nullable=False) 
    telefone = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    genero = Column(String(50), nullable=False)
    generico = Column(String(50), nullable=False)
    valor_de_comissao = Column(DECIMAL(10, 2), nullable=False)
    
    vendas = relationship("Venda", back_populates="cliente")