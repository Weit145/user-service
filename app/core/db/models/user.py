from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class User(Base):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(nullable=False)
    id_auth: Mapped[int] = mapped_column(nullable=False, unique=True)