from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime

class ModelBase(DeclarativeBase):
    data_criacao: Mapped[datetime] = mapped_column(default=datetime.now, index=True)