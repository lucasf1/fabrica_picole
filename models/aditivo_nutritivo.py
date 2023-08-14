from sqlalchemy import String, BIGINT
from sqlalchemy.orm import Mapped, mapped_column

from models.model_base import ModelBase


class AditivoNutritivo(ModelBase):
    __tablename__: str = 'aditivos_nutritivos'

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(45), unique=True, nullable=False)
    formula_quimica: Mapped[str] = mapped_column(String(45), unique=True, nullable=False)

    def __repr__(self):
        return f'<Aditivo Nutritivo: {self.nome}>'
