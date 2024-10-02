from typing import List

from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class Cat(Base):
    __tablename__ = "cat"

    id: Mapped[int] = mapped_column(primary_key=True)
    breed_id: Mapped[int] = mapped_column(ForeignKey("breed.id"))
    breed: Mapped["Breed"] = relationship(back_populates="cats")

class Breed(Base):
    __tablename__ = "breed"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    cats: Mapped[List["Cat"]] = relationship(back_populates="breed")

    