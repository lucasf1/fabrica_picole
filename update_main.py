"""
1 - Busca o registro a ser atualizado
2 - Faz as alterações
3 - Salva o registro no BD
"""

from conf.db_session import create_session

from models.sabor import Sabor
from models.picole import Picole

def select_filtro_picole(id_picole: int) -> None:
    with create_session() as session:

        picole: Picole = session.query(Picole).where(Picole.id == id_picole).one()

        if picole:
            print(f'ID: {picole.id}')
            print(f'Sabor: {picole.sabor.nome}')
        else:
            print(f"Não existe picolé com id: {id_picole}")

def atualizar_sabor(id_sabor: int, novo_sabor: str) -> None:
    with create_session() as session:
        # Passo 1
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()

        if sabor:
            # Passo 2
            sabor.nome = novo_sabor
            # Passo 3
            session.commit()
        else:
            print(f"Não existe sabor com id: {id_sabor}")

def atualizar_picole(id_picole: int, novo_preco: float, id_novo_sabor: int = None) -> None:
    with create_session() as session:
        # Passo 1
        picole: Picole = session.query(Picole).where(Picole.id == id_picole).one_or_none()

        if picole:
            # Passo 2
            picole.preco = novo_preco

            # Se quisermos o sabor também...
            if id_novo_sabor:
                picole.id_sabor = id_novo_sabor

            # Passo 3
            session.commit()
        else:
            print(f"Não existe picolé com id: {id_picole}")


if __name__ == "__main__":
    # from select_main import select_filtro_sabor
    #
    # id_sabor = 42
    #
    # # Antes
    # select_filtro_sabor(id_sabor=id_sabor)
    #
    # # Atualizando
    # atualizar_sabor(id_sabor=id_sabor, novo_sabor='Abacate')

    id_picole = 21
    novo_preco = 9.99
    id_novo_sabor = 42

    # Antes
    select_filtro_picole(id_picole=id_picole)

    # Atualizando
    atualizar_picole(id_picole=id_picole, novo_preco=novo_preco, id_novo_sabor=id_novo_sabor)

    # Depois
    select_filtro_picole(id_picole=id_picole)