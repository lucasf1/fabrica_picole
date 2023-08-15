from typing import List, Optional

import sqlalchemy as sa
from sqlalchemy import DECIMAL, ForeignKey, Table, Column, Integer, BIGINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.aditivo_nutritivo import AditivoNutritivo
from models.conservante import Conservante
from models.ingrediente import Ingrediente
from models.model_base import ModelBase
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole

# Picolé pode ter vários ingredientes
ingredientes_picoles = Table(
    'ingredientes_picole',
    ModelBase.metadata,
    Column('id_picole', Integer, ForeignKey('picoles.id')),
    Column('id_ingrediente', Integer, ForeignKey('ingredientes.id')),
)

# Picolé pode ter vários conservantes
conservantes_picoles = Table(
    'conservantes_picoles',
    ModelBase.metadata,
    Column('id_picole', Integer, ForeignKey('picoles.id')),
    Column('id_conservante', Integer, ForeignKey('conservantes.id')),
)

# Picolé pode ter vários aditivos nutritivos
aditivos_nutritivos_picole = Table(
    'aditivos_nutritivos_picole',
    ModelBase.metadata,
    Column('id_picole', Integer, ForeignKey('picoles.id')),
    Column('id_aditivo_nutritivo', Integer, ForeignKey('aditivos_nutritivos.id')),
)


class Picole(ModelBase):
    __tablename__: str = 'picoles'

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    preco: Mapped[float] = mapped_column(DECIMAL(8, 2), nullable=False)

    id_sabor: Mapped[int] = mapped_column(sa.ForeignKey('sabores.id'))
    sabor: Mapped[Sabor] = relationship('Sabor', lazy='joined')

    id_tipo_embalagem: Mapped[int] = mapped_column(ForeignKey('tipos_embalagem.id'))
    tipo_embalagem: Mapped[TipoEmbalagem] = relationship('TipoEmbalagem', lazy='joined')

    id_tipo_picole: Mapped[int] = mapped_column(ForeignKey('tipos_picole.id'))
    tipo_picole: Mapped[TipoPicole] = relationship('TipoEmbalagem', lazy='joined')

    # Um picolé pode ter vários ingredientes
    ingredientes: Mapped[List[Ingrediente]] = relationship('Ingrediente', secondary=ingredientes_picoles,
                                                           backref='ingrediente', lazy='joined')

    # Um picolé pode ter vários conservantes ou nenhum
    conservantes: Mapped[Optional[List[Conservante]]] = relationship('Conservante', secondary=conservantes_picoles,
                                                                     backref='conservante', lazy='joined')

    # Um picolé pode ter vários aditivos nutritivos ou nenhum
    aditivos_nutritivos: Mapped[Optional[List[AditivoNutritivo]]] = relationship('AditivoNutritivo',
                                                                                 secondary=aditivos_nutritivos_picole,
                                                                                 backref='aditivo_nutritivo',
                                                                                 lazy='joined')

    def __repr__(self):
        return f'<Picole: {self.tipo_picole.nome} com sabor {self.sabor.nome} e preço {self.preco}>'
