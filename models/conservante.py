import sqlalchemy as sa
from sqlalchemy import String, BIGINT
from sqlalchemy.orm import Mapped, mapped_column

from models.model_base import ModelBase


class Conservante(ModelBase):
    __tablename__: str = 'conservantes'

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(45), unique=True, nullable=False)
    descricao: Mapped[str] = mapped_column(sa.String(45), nullable=False)

    def __repr__(self):
        return f'<Conservante: {self.nome}>'
