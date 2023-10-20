from utils.create_db import create_db
from services.database import engine
from models import Cliente, Departamento, FormaDePagamento, Fornecedor, Funcionario, Manutencao, Produto, Venda, VendaProduto
from models import Base
from services.database import Session
from urllib.parse import quote
from datetime import datetime
from sqlalchemy import update

if __name__ == "__main__":
    create_db()

with Session(engine) as session:
    
    
    # Excluindo registros em Venda
    session.query(VendaProduto).delete()    
    session.query(Venda).delete()

    # Excluindo registros em Produto
    session.query(Produto).delete()

    # Excluindo registros em Manutencao
    session.query(Manutencao).delete()

    # Excluindo registros em Funcionario
    session.query(Funcionario).delete()

    # Excluindo registros em Cliente
    session.query(Cliente).delete()

    # Excluindo registros em FormasDePagamento
    session.query(FormaDePagamento).delete()

    # Excluindo registros em Fornecedor
    session.query(Fornecedor).delete()

    # Excluindo registros em Departamento
    session.query(Departamento).delete()

    # Confirmar as exclusões
    session.commit()

    
    # 1. CRIAR CLIENTES
    Marselo = Cliente(nome="Marselo", cpf="19456233827", telefone="(11) 1234-5678", email="marselofreire@gmail.com", genero="Masculino", generico="Masculino", valor_de_comissao=112)
    Leonardo = Cliente(nome="Leonardo", cpf="36729501842", telefone="(21) 9876-5432", email="leocaparica@gmail.com", genero="Masculino", generico="Masculino", valor_de_comissao=234)
    Donatelo = Cliente(nome="Donatelo", cpf="16385494420", telefone="(31) 5555-1234", email="donatelocamera@gmail.com", genero="Masculino", generico="Masculino", valor_de_comissao=40)
    Aparecida = Cliente(nome="Aparecida", cpf="60351747112", telefone="(41) 7890-1234", email="Cidasouza@gmail.com", genero="Femenino", generico="Femenino", valor_de_comissao=50)
    Fabrisio = Cliente(nome="Fabrisio", cpf="30155822524", telefone="(51) 2345-6789", email="fabrisiopinterest@gmail.com", genero="Masculino", generico="Masculino", valor_de_comissao=252)
    Ruan = Cliente(nome="Ruan", cpf="43543054305", telefone="(31) 2446-6789", email="ruanenzo@gmail.com", genero="Masculino", generico="Masculino", valor_de_comissao=30)


    session.add_all([Marselo, Leonardo, Donatelo, Aparecida, Fabrisio, Ruan])
    session.commit()

    # 2. CRIAR DEPARTAMENTO
    RoupasFemininas = Departamento(nome="Roupas Femininas", genero="Moda Feminina")
    RoupasMasculina = Departamento(nome="Roupas Masculinas", genero="Moda Masculina")
    RoupasInfantis = Departamento(nome="Roupas Infantis", genero="Moda Infantil")
    RoupasEsportivas = Departamento(nome="Roupas Esportivas", genero="Moda Esportiva")
    RoupasCasuais = Departamento(nome="Roupas Casuais", genero="Moda Casual")
    RoupasFormais = Departamento(nome="Roupas Formais", genero="Moda Formal")

    session.add_all([RoupasFemininas, RoupasMasculina, RoupasInfantis, RoupasEsportivas, RoupasCasuais, RoupasFormais])
    session.commit()

    # 3. CRIAR FORMAS DE PAGAMENTO
    Dinheiro = FormaDePagamento(nome="Dinheiro", tipo_de_forma_de_pagamento="Pagamento em Dinheiro")
    CartaoDeCredito = FormaDePagamento(nome="Cartão de Credito", tipo_de_forma_de_pagamento="Pagamento com cartão de credito")
    CartaoDeDebito = FormaDePagamento(nome="Cartão de Debito", tipo_de_forma_de_pagamento="Pagamento com cartão de debito")
    Boleto = FormaDePagamento(nome="Boleto Bancaria", tipo_de_forma_de_pagamento="Pagamento com boleto bancaria")
    Criptomoedas = FormaDePagamento(nome="Criptomoedas", tipo_de_forma_de_pagamento="Pagamento com criptomoedas")
    Cupons = FormaDePagamento(nome="Cupons", tipo_de_forma_de_pagamento ="Pagamento com Cupons")

    session.add_all([Dinheiro, CartaoDeCredito, CartaoDeDebito, Boleto, Criptomoedas, Cupons])
    session.commit()

    # 4. CRIAR FORNECEDOR
    Odin = Fornecedor(cnpj="12345678000190", nome_da_empresa="Fornecodr Odin", tipo_de_produto="Camisa", quantidade_de_produto="30", valor=5000)
    Zeus = Fornecedor(cnpj="98765432000121", nome_da_empresa="Fornecodr Zeus", tipo_de_produto="Bolsa", quantidade_de_produto="10", valor=18000)
    Tyche = Fornecedor(cnpj="11222333000144", nome_da_empresa="Fornecodr Tyche", tipo_de_produto="Salto", quantidade_de_produto="47", valor=5300)
    Loki = Fornecedor(cnpj="55666777000188", nome_da_empresa="Fornecodr Loki", tipo_de_produto="Calça", quantidade_de_produto="25", valor=9405)
    Aphrodite = Fornecedor(cnpj="99888777000133", nome_da_empresa="Fornecodr Aphrodite", tipo_de_produto="Cueca", quantidade_de_produto="53", valor=85)
    Hades = Fornecedor(cnpj="77555444000166", nome_da_empresa="Fornecodr Hades", tipo_de_produto="Cinto", quantidade_de_produto="23", valor=490)

    session.add_all([Odin, Zeus, Tyche, Loki, Aphrodite, Hades])
    session.commit()

    # 5. CRIAR FUNCIONÁRIO
    Joao = Funcionario(nome="Joao", cpf="98765432100", conta="Conta123", salario=3000.00, carga_horaria="40:00:00", endereco="Rua das Flores, 123, Bairro Felicidade", funcao="Vendedor", comissao=2000, departamento=RoupasFemininas, manutencao_id=None)
    Claudia = Funcionario(nome="Claudia", cpf="98765432121", conta="Conta234", salario=3000.00, carga_horaria="45:00:00", endereco="Avenida dos Sonhos, 456, Bairro Esperança", funcao="Vendedor", comissao=2000, departamento=RoupasMasculina, manutencao_id=None)
    GuiFalks = Funcionario(nome="Guilherme Facao", cpf="11122233344", conta="Conta345", salario=7000.00, carga_horaria="50:00:00", endereco="Praça da Imaginação, 789, Bairro Fantasia", funcao="Gerente", comissao=2000, departamento=RoupasInfantis, manutencao_id=None)
    Carlos = Funcionario(nome="Carlos", cpf="55566677788", conta="Conta456", salario=3000.00, carga_horaria="45:00:00", endereco="Estrada da Aventura, 234, Bairro Alegria", funcao="Vendedor", comissao=2000, departamento=RoupasEsportivas, manutencao_id=None)
    Henrique = Funcionario(nome="Henrique", cpf="99988877733", conta="Conta567", salario=3000.00, carga_horaria="40:00:00", endereco="Alameda da Fantasia, 567, Bairro Felizville", funcao="Vendedor", comissao=2000, departamento=RoupasCasuais, manutencao_id=None)
    Thiaguinho = Funcionario(nome="Thiaguinho", cpf="77755544466", conta="Conta678", salario=3000.00, carga_horaria="45:00:00", endereco="Travessa dos Sonhos, 890, Bairro Alegreza", funcao="Vendedor", comissao=2000, departamento=RoupasFormais, manutencao_id=None)

    session.add_all([Joao, Claudia, GuiFalks, Carlos, Henrique, Thiaguinho])
    session.commit()

    # 6. CRIAR MANUTENÇÃO
    manutencaoA = Manutencao(nome="Manutenção A", setor="Limpeza e Venda")
    manutencaoB = Manutencao(nome="Manutenção B", setor="Limpeza e Venda")
    manutencaoC = Manutencao(nome="Manutenção C", setor="Gerente")
    manutencaoD = Manutencao(nome="Manutenção D", setor="Limpeza e Venda")
    manutencaoE = Manutencao(nome="Manutenção E", setor="Limpeza e Venda")
    manutencaoF = Manutencao(nome="Manutenção F", setor="Limpeza e Venda")
    
    session.add_all([manutencaoA, manutencaoB, manutencaoC, manutencaoD, manutencaoE, manutencaoF])
    
    manutencaoA.funcionario = Joao
    manutencaoB.funcionario = Claudia
    manutencaoC.funcionario = GuiFalks
    manutencaoD.funcionario = Carlos
    manutencaoE.funcionario = Henrique
    manutencaoF.funcionario = Thiaguinho

    session.commit()

    # 7. CRIAR PRODUTO
    Camisa = Produto(nome="camisa", tipo="roupa", marca="Prada", genero="feminino", tamanho="PP/P/M/G/GG", valor= 5000.00, comissao=250.00, quantidade=30, fornecedor_id=Odin.id) 
    Bolsa = Produto(nome="bolsa", tipo="acessorios", marca="Alexander Mcqueen", genero="feminino", tamanho="unico", valor= 18.000, comissao=900.00, quantidade=10, fornecedor_id=Zeus.id)
    Salto = Produto(nome="salto", tipo="salto", marca="Christian Dior", genero="feminino", tamanho="35/36/37/38", valor= 5300.00, comissao=265.00, quantidade=47, fornecedor_id=Tyche.id)
    Calça = Produto(nome="calça", tipo="roupa", marca="Balmain", genero="masculino", tamanho="PP/P/M/G/GG", valor= 9.405, comissao=470.25, quantidade=25, fornecedor_id=Loki.id)
    Cueca = Produto(nome="cueca", tipo="roupa", marca="Calvin Klein", genero="masculino", tamanho="PP/P/M/G/GG", valor= 85.00, comissao=4.25, quantidade=53, fornecedor_id=Aphrodite.id)
    Cinto = Produto(nome="cinto", tipo="acessorios", marca="Balenciaga", genero="masculino", tamanho="unico", valor= 490.00, comissao=24.50, quantidade=23, fornecedor_id=Hades.id)

    session.add_all([Camisa, Bolsa, Salto, Calça, Cueca, Cinto])
    session.commit()

    # 8. CRIAR VENDA
    venda1 = Venda(data=datetime.now(), valor=10000, cliente_id=Marselo.id, forma_de_pagamento_id=Dinheiro.id, funcionario_id=Joao.id)
    venda2 = Venda(data=datetime.now(), valor=18900, cliente_id=Leonardo.id, forma_de_pagamento_id=CartaoDeCredito.id, funcionario_id=Claudia.id)
    venda3 = Venda(data=datetime.now(), valor=24790, cliente_id=Donatelo.id, forma_de_pagamento_id=CartaoDeDebito.id, funcionario_id=GuiFalks.id)
    venda4 = Venda(data=datetime.now(), valor=30000, cliente_id=Aparecida.id, forma_de_pagamento_id=Boleto.id, funcionario_id=Carlos.id)
    venda5 = Venda(data=datetime.now(), valor=12000, cliente_id=Fabrisio.id, forma_de_pagamento_id=Criptomoedas.id, funcionario_id=Henrique.id)
    venda6 = Venda(data=datetime.now(), valor=24000, cliente_id=Ruan.id, forma_de_pagamento_id=Cupons.id, funcionario_id=Thiaguinho.id)
    
    session.add_all([venda1, venda2, venda3, venda4, venda5, venda6])
    session.commit()

    #9 CRIAR VENDA_PRODUTO
    venda_produto1 = VendaProduto(venda_id=venda1.id, produto_id=Camisa.id)
    venda_produto2 = VendaProduto(venda_id=venda2.id, produto_id=Bolsa.id)
    venda_produto3 = VendaProduto(venda_id=venda3.id, produto_id=Salto.id)
    venda_produto4 = VendaProduto(venda_id=venda4.id, produto_id=Calça.id)
    venda_produto5 = VendaProduto(venda_id=venda5.id, produto_id=Cueca.id)
    venda_produto6 = VendaProduto(venda_id=venda6.id, produto_id=Cinto.id)
    
    session.add_all([venda_produto1, venda_produto2, venda_produto3, venda_produto4, venda_produto5, venda_produto6])
    session.commit()
    
    with engine.begin() as conn:

        conn.execute(update(Cliente).where(Cliente.id == Marselo.id).values(email="marselotuba@viado.com.br"))

        conn.execute(update(Departamento).where(Departamento.id == RoupasInfantis.id).values(nome="Roupas Plus Size", genero="Moda Plus Size"))

        conn.execute(update(FormaDePagamento).where(FormaDePagamento.id == Cupons.id).values(nome="Pix"))

        conn.execute(update(Fornecedor).where(Fornecedor.id == Zeus.id).values(nome_da_empresa="Freia", valor=20000))

        conn.execute(update(Funcionario).where(Funcionario.id == GuiFalks.id).values(nome="Murilo", funcao="Gerencia"))

        conn.execute(update(Manutencao).where(Manutencao.id == manutencaoA.id).values(setor="Empacotador"))

        conn.execute(update(Produto).where(Produto.id == Cueca.id).values(nome="Lingerie", tamanho="PP/P/M/G/GG/XL", valor=999.99))

        conn.execute(update(Venda).where(Venda.id == venda1.id).values(data="2023-12-22"))
        
Produtos = session.query(Produto, Fornecedor).join(Fornecedor, Produto.fornecedor_id == Fornecedor.id)
vendas = session.query(Venda, Cliente, FormaDePagamento, Funcionario).join(Cliente).join(FormaDePagamento).join(Funcionario)
vendasProdutos = session.query(VendaProduto, Venda, Produto).join(Venda).join(Produto)
Funcionarios = session.query(Funcionario, Departamento, Manutencao).join(Departamento).join(Manutencao)

clientes = session.query(Cliente).all()
print("\nConsulta numero 1 tabela Cliente")
for cliente in clientes:
    print(f"\nID: {cliente.id}")
    print(f"Nome: {cliente.nome}")
    print(f"CPF: {cliente.cpf}")
    print(f"Telefone: {cliente.telefone}")
    print(f"Email: {cliente.email}")
    print(f"Genero: {cliente.genero}")
    print(f"Generico: {cliente.generico}")
    print(f"Valor De Comissao: {cliente.valor_de_comissao}\n")
    
Departamento = session.query(Departamento).all()
print("\nConsulta numero 2 tabela Departamento")
for departamento in Departamento:
    print(f"\nID: {departamento.id}")
    print(f"Nome: {departamento.nome}")
    print(f"Genero: {departamento.genero}\n")
    
FormaDePagamento = session.query(FormaDePagamento).all()
print("\nConsulta numero 3 tabela Formas de Pagamento")
for FormaDePagamento in FormaDePagamento:
    print(f"\nID: {FormaDePagamento.id}")
    print(f"Nome: {FormaDePagamento.nome}")
    print(f"Genero: {FormaDePagamento.tipo_de_forma_de_pagamento}\n")
    
Fornecedor = session.query(Fornecedor).all()
print("\nConsulta numero 4 tabela de Fornecedores")
for Fornecedor in Fornecedor:
    print(f"\nID: {Fornecedor.id}")
    print(f"CNPJ: {Fornecedor.cnpj}")
    print(f"Nome da Empresa: {Fornecedor.nome_da_empresa}")
    print(f"Qual o Produto: {Fornecedor.tipo_de_produto}")
    print(f"Quantidade Fornecida: {Fornecedor.quantidade_de_produto}\n")
    
print("Consulta número 5 tabela de Funcionarios")
for funcionario, departamento, manutencao in Funcionarios:
    print(f"ID: {funcionario.id}")
    print(f"Nome: {funcionario.nome}")
    print(f"CPF: {funcionario.cpf}")
    print(f"Conta: {funcionario.conta}")
    print(f"Salario: {funcionario.salario}")
    print(f"Carga Horaria: {funcionario.carga_horaria}")
    print(f"Endereço: {funcionario.endereco}")
    print(f"Função: {funcionario.funcao}")
    print(f"Comissão: {funcionario.comissao}")
    print(f"Departamento: {departamento.nome}")


    
Manutencao = session.query(Manutencao).all()
print("\nConsulta numero 6 tabela de Manutenção")
for Manutencao in Manutencao:
    print(f"\nID: {Manutencao.id}")
    print(f"Nome: {Manutencao.nome}")
    print(f"Setor: {Manutencao.setor}\n")
    
Produto = session.query(Produto).all()
print(".")
print("\nConsulta numero 7 tabela de Produtos")
for produto, fornecedor in Produtos:
    print(f"\nID: {produto.id}")
    print(f" Nome: {produto.nome}")
    print(f"Tipo de Produto: {produto.tipo}")
    print(f"Marca: {produto.marca}")
    print(f"Gênero: {produto.genero}")
    print(f"Tamanho: {produto.tamanho}")
    print(f"Valor: {produto.valor}")
    print(f"Comissão: {produto.comissao}")
    print(f"Quantidade De Produtos: {produto.quantidade}")
    print(f"Fornecedor: {fornecedor.nome_da_empresa}\n")
    
Venda = session.query(Venda).all()
print("\nConsulta numero 8 tabela de Venda")
for Venda, cliente, FormaDePagamento, Funcionario in vendas:
    print(f"\nID: {Venda.id}")
    print(f"Data: {Venda.data}")
    print(f"Valor: {Venda.valor}")
    print(f"Cliente: {cliente.nome}")
    print(f"Forma De Pagamento: {FormaDePagamento.nome}")
    print(f"Funcionario: {Funcionario.nome}\n")
    
print("\nConsulta numero 9 tabela de VendaProduto")
for venda_produto, venda, produto in vendasProdutos:
    print(f"\nID: {venda_produto.id}")
    print(f"Venda ID: {venda.id}")
    print(f"Produto ID: {produto.id}\n")
    
    
print("Quais são os dados dos clientes com valor de comissão acima de 100?\n")

clientes_com_comissao_acima_de_100 = session.query(Cliente).filter(Cliente.valor_de_comissao > 100).all()
for cliente in clientes_com_comissao_acima_de_100:
    print("ID:", cliente.id)
    print("Nome:", cliente.nome)
    print("CPF:", cliente.cpf)
    print("Telefone:", cliente.telefone)
    print("Email:", cliente.email)
    print("Valor de Comissão:", cliente.valor_de_comissao)
    print("\n")
    
print("Quais são os dados dos Funcionarios com Salario acima de 3000?\n")

salario_maior_que_3000 = session.query(Funcionario).filter(Funcionario.salario > 3000).all()
for funcio in salario_maior_que_3000:
    print("ID:", Funcionario.id)
    print("Nome:", Funcionario.nome)
    print("CPF:", Funcionario.cpf)
    print("Conta:", Funcionario.conta)
    print("Carga Horaria:", Funcionario.carga_horaria)
    print("Endereço:", Funcionario.endereco)
    print("Função:", Funcionario.funcao)
    print("Valor de Comissão:", Funcionario.comissao)
    print("\n")

session.close()