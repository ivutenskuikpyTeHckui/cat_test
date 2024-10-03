from sqlalchemy import select, delete, update
from sqlalchemy.orm import selectinload, joinedload

from src.cat.models import Cat, Breed

from src.database import async_session_maker

from src.cat.schemas import (
    Create_cat_model,
    Edit_cat_model,
    Create_breed_model,
    Edit_breed_model
)


class CatRepository:

    @staticmethod
    async def create_cat(
        new_cat_model:Create_cat_model,
    ) -> Cat:
        async with async_session_maker() as session:
            cat = Cat(**new_cat_model.model_dump())

            session.add(cat)

            await session.commit()

            return cat
        
    @staticmethod
    async def get_all_cats() -> list[Cat]:
        async with async_session_maker() as session:
            query = (
                select(Cat).
                options(
                    joinedload(Cat.breed),
                ).
                order_by(Cat.id)
            )

            all_cats = await session.scalars(query)
            
            return list(all_cats)

class BreedRepository:

    @staticmethod
    async def create_breed(
        new_breed_model:Create_breed_model,
    ) -> Breed:
        async with async_session_maker() as session:
            breed = Breed(**new_breed_model.model_dump())
            session.add(breed)
            await session.commit()

            return breed
        
    @staticmethod
    async def get_all_breeds() -> list[Breed]:
        async with async_session_maker() as session:
            query = (
                select(Breed).
                order_by(Breed.id)
            )

            all_breeds = await session.scalars(query)
            
            return list(all_breeds)
