from models.cliente import Cliente
from models.departamento import Departamento
from models.formas_de_pagamento import FormaDePagamento
from models.fornecedor import Fornecedor
from models.funcionario import Funcionario
from models.manutencao import Manutencao
from models.produto import Produto
from models.venda import Venda
from models.venda_produto import VendaProduto
from services.database import engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def create_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)