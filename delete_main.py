"""
1 - Busca o registro a ser deletado
2 - Fazer as deleção do objeto a ser encontrado
3 - Registrar no BD a deleção
"""

from conf.db_session import create_session

from typing import List, Optional

from models.revendedor import Revendedor
from models.picole import Picole


def deletar_picole(id_picole: int) -> None:
    with create_session() as session:
        # Passo1
        picole: Optional[Picole] = session.query(Picole).where(Picole.id == id_picole).one_or_none()

        if picole:
            # Passo 2
            session.delete(picole)
            # Passo 3
            session.commit()
        else:
            print(f"Não encontrei picolé com id: {id_picole}")

def deletar_revendedor(id_revendedor: int) -> None:
    with create_session() as session:
        revendedor: Optional[Revendedor] = session.query(Revendedor).where(Revendedor.id == id_revendedor).one_or_none()

        if revendedor:
            session.delete(revendedor)
            session.commit()
        else:
            print(f'Não encontrei nenhum revendedor com ID: {id_revendedor}')

def select_filtro_revendedor(id_revendedor: int) -> None:
    with create_session() as session:
        revendedor: Optional[Revendedor] = session.query(Revendedor).where(Revendedor.id == id_revendedor).one_or_none()

        if revendedor:
            print(f'ID: {revendedor.id}')
            print(f'Razão Social: {revendedor.razao_social}')
        else:
            print(f'Não encontrei nenhum revendedor com ID: {id_revendedor}')


if __name__ == "__main__":
    # from update_main import select_filtro_picole
    #
    # id_picole = 21
    #
    # # Antes
    # select_filtro_picole(id_picole=id_picole)
    #
    # # Deletar
    # deletar_picole(id_picole=id_picole)
    #
    # # Depois
    # select_filtro_picole(id_picole=id_picole)

    # não vinculado
    id_revendedor_nv = 5

    # vinculado
    id_revendedor_v = 6

    # # Antes
    # select_filtro_revendedor(id_revendedor=id_revendedor_nv)
    #
    # # Deletar
    # deletar_revendedor(id_revendedor=id_revendedor_nv)
    #
    # # Depois
    # select_filtro_revendedor(id_revendedor=id_revendedor_nv)

    # Antes
    select_filtro_revendedor(id_revendedor=id_revendedor_v)

    # Deletar
    deletar_revendedor(id_revendedor=id_revendedor_v)

    # Depois
    select_filtro_revendedor(id_revendedor=id_revendedor_v)