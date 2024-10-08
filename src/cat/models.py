from typing import List

from sqlalchemy import ForeignKey, String

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class Cat(Base):
    __tablename__ = "cat"

    id: Mapped[int] = mapped_column(primary_key=True)
    color: Mapped[str] = mapped_column(String(24))
    age: Mapped[int]
    description: Mapped[str] = mapped_column(String(256))
    breed_id: Mapped[int] = mapped_column(ForeignKey("breed.id", ondelete="CASCADE"))
    breed: Mapped["Breed"] = relationship(back_populates="cats")

    def __str__(self) -> str:
        return f"id = {self.id}, color = {self.color}, age = {self.age}, description = {self.description}, breed_id = {self.breed_id}"

    def __repr__(self) -> str:
        return str(self)

class Breed(Base):
    __tablename__ = "breed"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    cats: Mapped[List["Cat"]] = relationship(back_populates="breed")

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return str(self)
    
