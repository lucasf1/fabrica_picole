from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, BIGINT

from models.model_base import ModelBase
from models.tipo_picole import TipoPicole


class Lote(ModelBase):
    __tablename__: str = 'lotes'

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)

    id_tipo_picole: Mapped[int] = mapped_column(ForeignKey('tipos_picole.id'))  # tabela.campo
    tipo_picole: Mapped[TipoPicole] = relationship(lazy='joined') # conf interna do SQL Alchemy

    quantidade: Mapped[int] = mapped_column(nullable=False)

    def __repr__(self):
        return f'<Lote: {self.id}>'
