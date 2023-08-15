from conf.db_session import create_session
# Insert parte 1
from models.aditivo_nutritivo import AditivoNutritivo
from models.conservante import Conservante
from models.ingrediente import Ingrediente
# Insert parte 2
from models.lote import Lote
from models.nota_fiscal import NotaFiscal
from models.picole import Picole
from models.revendedor import Revendedor
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole


# 1 Aditivo Nutritivo
def insert_aditivo_nutritivo() -> AditivoNutritivo:
    print("Cadastrando Aditivo Nutritivo")

    nome: str = input("Informe o nome do Aditivo Nutritivo: ")
    formula_quimica: str = input("Informe a fórmula química: ")

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    with create_session() as session:
        session.add(an)
        session.commit()

    # print("Aditivo Nutritivo cadastrado com sucesso.")
    # print(f"ID: {an.id}")
    # print(f"Data de Criação: {an.data_criacao}")
    # print(f"Nome: {an.nome}")
    # print(f"Fórmula Química: {an.formula_quimica}")
    return an

# 2 Sabor
def insert_sabor():
    print("Cadastrando Sabor")

    nome: str = input("Informe o nome do Sabor: ")

    sabor: Sabor = Sabor(nome=nome)

    with create_session() as session:
        session.add(sabor)
        session.commit()

    print("Sabor cadastrado com sucesso.")
    print(f"ID: {sabor.id}")
    print(f"Data de Criação: {sabor.data_criacao}")
    print(f"Nome: {sabor.nome}")


# 3 Tipo Embalagem
def insert_tipo_embalagem():
    print("Cadastrando Tipo de Embalagem")

    nome: str = input("Informe o nome do Tipo de Embalagem: ")

    te: TipoEmbalagem = TipoEmbalagem(nome=nome)

    with create_session() as session:
        session.add(te)
        session.commit()

    print("Tipo de Embalagem cadastrado com sucesso.")
    print(f"ID: {te.id}")
    print(f"Data de Criação: {te.data_criacao}")
    print(f"Nome: {te.nome}")


# 4 Tipo Picole
def insert_tipo_picole():
    print("Cadastrando Tipo de Picolé")

    nome: str = input("Informe o nome do Tipo de Picolé: ")

    tp: TipoPicole = TipoPicole(nome=nome)

    with create_session() as session:
        session.add(tp)
        session.commit()

    print("Tipo de Picolé cadastrado com sucesso.")
    print(f"ID: {tp.id}")
    print(f"Data de Criação: {tp.data_criacao}")
    print(f"Nome: {tp.nome}")


# 5 Ingrediente
def insert_ingrediente() -> Ingrediente:
    print("Cadastrando Ingrediente")

    nome: str = input("Informe o nome do Ingrediente: ")

    ingr: Ingrediente = Ingrediente(nome=nome)

    with create_session() as session:
        session.add(ingr)
        session.commit()

    # print("Ingrediente cadastrado com sucesso.")
    # print(f"ID: {ingr.id}")
    # print(f"Data de Criação: {ingr.data_criacao}")
    # print(f"Nome: {ingr.nome}")
    return ingr


# 6 Conservante
def insert_conservante() -> Conservante:
    print("Cadastrando Conservante")

    nome: str = input("Informe o nome do Conservante: ")
    descricao: str = input("Informe a descrição: ")

    cons: Conservante = Conservante(nome=nome, descricao=descricao)

    with create_session() as session:
        session.add(cons)
        session.commit()

    # print("Conservante cadastrado com sucesso.")
    # print(f"ID: {cons.id}")
    # print(f"Data de Criação: {cons.data_criacao}")
    # print(f"Nome: {cons.nome}")
    # print(f"Descrição: {cons.descricao}")
    return cons

# 7 Revendendor
def insert_revendendor() -> Revendedor:
    print("Cadastrando Revendendor")

    cnpj: str = input("Informe o cnpj do Revendendor: ")
    razao_social: str = input("Informe a razão social do Revendendor: ")
    contato: str = input("Informe o contato do Revendendor: ")

    rev: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)

    with create_session() as session:
        session.add(rev)
        session.commit()

    print("Revendedor cadastrado com sucesso.")
    return rev


# 8 Lote
def insert_lote() -> Lote:
    print("Cadastrando Lote")

    id_tipo_picole: int = input("Informe o id do tipo de picolé: ")
    quantidade: int = input("Informe a quantidadade: ")

    lote: Lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)

    with create_session() as session:
        session.add(lote)
        session.commit()

    print("Lote cadastrado com sucesso.")
    return lote


# 9 Nota Fiscal
def insert_nota_fiscal() -> None:
    print("Cadastrando Nota Fiscal")

    valor: float = input("Informe o valor da nota fiscal: ")
    numero_serie: str = input("Informe o número de série: ")
    descricao: str = input("Informe a descrição: ")
    # id_revendedor: int = input("Informe o ID do revendedor: ")

    rev = insert_revendendor()
    id_revendedor = rev.id

    nf: NotaFiscal = NotaFiscal(valor=valor, numero_serie=numero_serie, descricao=descricao,
                                id_revendedor=id_revendedor)

    lote1 = insert_lote()
    nf.lotes.append(lote1)

    lote2 = insert_lote()
    nf.lotes.append(lote2)

    with create_session() as session:
        session.add(nf)
        session.commit()

    print("Nota fiscal cadastrada com sucesso.")
    print(f"ID: {nf.id}")
    print(f"Data de criação: {nf.data_criacao}")
    print(f"Valor: {nf.valor}")
    print(f"Número de série: {nf.numero_serie}")
    print(f"Descrição: {nf.descricao}")
    print(f"ID Revendedor: {nf.id_revendedor}")
    print(f"Revendedor: {nf.revendedor.razao_social}")


# 10 Picolé
def insert_picole() -> None:
    print("Cadastrando Picolé")

    preco: float = input("Informe o preço do picolé: ")
    id_sabor: int = input("Informe o ID do sabor: ")
    id_tipo_picole: int = input("Informe o ID do tipo do picolé: ")
    id_tipo_embalagem: int = input("Informe o ID do tipo da embalagem: ")

    picole: Picole = Picole(preco=preco, id_sabor=id_sabor, id_tipo_picole=id_tipo_picole,
                            id_tipo_embalagem=id_tipo_embalagem)

    ingrediente1 = insert_ingrediente()
    picole.ingredientes.append(ingrediente1)
    ingrediente2 = insert_ingrediente()
    picole.ingredientes.append(ingrediente2)

    # Tem conservante
    conservante = insert_conservante()
    picole.conservantes.append(conservante)

    # Tem aditivo nutritivo
    aditivo_nutritivo = insert_aditivo_nutritivo()
    picole.aditivos_nutritivos.append(aditivo_nutritivo)

    with create_session() as session:
        session.add(picole)
        session.commit()

    print("Picolé cadastrado com sucesso.")
    print(f"ID: {picole.id}")
    print(f"Data de criação: {picole.data_criacao}")
    print(f"Preco: {picole.preco}")
    print(f"Sabor: {picole.sabor.nome}")
    print(f"Tipo Picolé: {picole.tipo_picole.nome}")
    print(f"Tipo da Embalagem: {picole.tipo_embalagem.nome}")
    print(f"Ingredientes: {picole.ingredientes}")
    print(f"Conservantes: {picole.conservantes}")
    print(f"Aditivos Nutritivos: {picole.aditivos_nutritivos}")


if __name__ == "__main__":
    # 1 Aditivo Nutritivo
    # insert_aditivo_nutritivo()

    # 2 Sabor
    # insert_sabor()

    # 3 Tipo Embalagem
    # insert_tipo_embalagem()

    # 4 Tipo Picolé
    # insert_tipo_picole()

    # 5 Ingrediente
    # insert_ingrediente()

    # 6 Conservante
    # insert_conservante()

    # 7 Revendendor
    # rev = insert_revendendor()
    # print(f"ID: {rev.id}")
    # print(f"Data de Criação: {rev.data_criacao}")
    # print(f"CNPJ: {rev.cnpj}")
    # print(f"Razão Social: {rev.razao_social}")
    # print(f"Contato: {rev.contato}")

    # 8 Lote
    # lote = insert_lote()
    # print(f"ID: {lote.id}")
    # print(f"Data de Criação: {lote.data_criacao}")
    # print(f"ID tipo de picolé: {lote.id_tipo_picole}")
    # print(f"Quantidade: {lote.quantidade}")

    # 9 Nota Fiscal
    # insert_nota_fiscal()

    # 10 Picolé
    insert_picole()