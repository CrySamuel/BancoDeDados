from sqlalchemy import Column, Integer, String, CHAR, DECIMAL, TIME, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models import Base
from models.manutencao import Manutencao

class Funcionario(Base):
    __tablename__ = "funcionario"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(CHAR(11), nullable=False, unique=True)
    conta = Column(String(50), nullable=False)
    salario = Column(DECIMAL(10, 2), nullable=False)
    carga_horaria = Column(TIME, nullable=False)
    endereco = Column(String(100), nullable=False)
    funcao = Column(String(50), nullable=False)
    comissao = Column(DECIMAL(10, 2), nullable=False)
    departamento_id = Column(Integer, ForeignKey('departamento.id'))
    manutencao_id = Column(Integer, ForeignKey('manutencao.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=True)

    departamento = relationship('Departamento', back_populates='funcionarios')
    manutencoes = relationship("Manutencao")
