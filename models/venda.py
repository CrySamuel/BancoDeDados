from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func
from models.base import Base
from services.database import engine

class Venda(Base):
    __tablename__ = 'venda'

    id = Column(Integer, primary_key=True)
    data = Column(DateTime, default=func.now())
    valor = Column(Float)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))
    forma_de_pagamento_id = Column(Integer, ForeignKey('formas_de_pagamento.id'))
    funcionario_id = Column(Integer, ForeignKey('funcionario.id'))

    cliente = relationship("Cliente")
    forma_de_pagamento = relationship("FormaDePagamento")
    funcionario = relationship("Funcionario")
