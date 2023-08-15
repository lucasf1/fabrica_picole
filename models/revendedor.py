from sqlalchemy import String, BIGINT
from sqlalchemy.orm import mapped_column, Mapped

from models.model_base import ModelBase


class Revendedor(ModelBase):
    __tablename__: str = 'revendedores'

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)

    cnpj: Mapped[str] = mapped_column(String(45), unique=True, nullable=False)
    razao_social: Mapped[str] = mapped_column(String(100), nullable=False)
    contato: Mapped[str] = mapped_column(String(100), nullable=False)

    def __repr__(self):
        return f'<Revendedor: {self.nome}>'
