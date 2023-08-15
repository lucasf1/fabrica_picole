from typing import List

from sqlalchemy import DECIMAL, String, ForeignKey, Table, Column, Integer, BIGINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.lote import Lote
from models.model_base import ModelBase
from models.revendedor import Revendedor

# nota fiscal pode ter vários lotes
lotes_nota_fiscal = Table(
    'lotes_nota_fiscal',
    ModelBase.metadata,
    Column('id_nota_fiscal', Integer, ForeignKey('notas_fiscais.id')),
    Column('id_lote', Integer, ForeignKey('lotes.id'))
)


class NotaFiscal(ModelBase):
    __tablename__: str = 'notas_fiscais'

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)

    valor: Mapped[float] = mapped_column(DECIMAL(8, 2), nullable=False)
    numero_serie: Mapped[str] = mapped_column(String(45), unique=True, nullable=False)
    descricao: Mapped[str] = mapped_column(String(200), nullable=False)

    id_revendedor: Mapped[int] = mapped_column(ForeignKey('revendedores.id'))
    revendedor: Mapped[Revendedor] = relationship('Revendedor', lazy='joined')

    # Uma nota fiscal pode ter vários lotes e um lote está ligado a uma nota fiscal
    lotes: Mapped[List[Lote]] = relationship('Lote', secondary=lotes_nota_fiscal, backref='lote', lazy='dynamic')

    def __repr__(self):
        return f'<Nota Fiscal: {self.numero_serie}>'
