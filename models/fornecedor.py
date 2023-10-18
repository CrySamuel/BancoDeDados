from sqlalchemy import Column, Integer, String, CHAR, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models import Base 

class Fornecedor(Base):
    __tablename__ = "fornecedor" 

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    cnpj = Column(CHAR(14), nullable=False)
    nome_da_empresa = Column(String(100), nullable=False)
    tipo_de_produto = Column(String(50), nullable=False)
    quantidade_de_produto = Column(Integer, nullable=False)
    valor = Column(DECIMAL(10, 2), nullable=False)
    
    produtos = relationship("Produto", back_populates="fornecedor")