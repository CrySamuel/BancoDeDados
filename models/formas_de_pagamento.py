from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models import Base  

class FormaDePagamento(Base):
    __tablename__ = "formas_de_pagamento"  

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = Column(String(100), nullable=False)
    tipo_de_forma_de_pagamento = Column(String(100), nullable=False)
    
    vendas = relationship("Venda", back_populates="forma_de_pagamento")
