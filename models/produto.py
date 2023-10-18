from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship 
from models import Base

class Produto(Base):
    __tablename__ = "produto"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = Column(String(100), nullable=False)
    tipo = Column(String(50), nullable=False)
    marca = Column(String(50))
    genero = Column(String(50), nullable=False)
    tamanho = Column(String(50), nullable=False)
    valor = Column(DECIMAL(10, 2), nullable=False)
    comissao = Column(DECIMAL(10, 2), nullable=False)
    quantidade = Column(Integer, nullable=False)
    fornecedor_id = Column(Integer, ForeignKey('fornecedor.id'))

    fornecedor = relationship("Fornecedor", back_populates="produtos")
    vendas = relationship("Venda", secondary="venda_produto")
