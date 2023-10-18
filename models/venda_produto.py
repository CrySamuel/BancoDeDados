from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class VendaProduto(Base):
    __tablename__ = 'venda_produto'
    
    id = Column(Integer, primary_key=True)
    venda_id = Column(Integer, ForeignKey('venda.id'))
    produto_id = Column(Integer, ForeignKey('produto.id'))
    

    venda = relationship('Venda', backref='venda_produtos')
    produto = relationship('Produto', backref='venda_produtos')
