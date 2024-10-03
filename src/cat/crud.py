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
            stmt = Cat(**new_cat_model.model_dump())

            session.add(stmt)

            await session.commit()

            return stmt
        
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
        
    @staticmethod
    async def get_cat_by_id(
        cat_id:int
) -> Cat:
        async with async_session_maker() as session:
            query = (
                select(Cat).
                where(Cat.id==cat_id).
                options(
                    joinedload(Cat.breed),
                ).
                order_by(Cat.id)
            )
            cat = await session.scalar(query)

            return cat

    @staticmethod
    async def edit_cat(
        cat_id:int,
        cat_edit:Edit_cat_model
):
        async with async_session_maker() as session:
            stmt = (
                update(Cat).
                where(Cat.id==cat_id).
                values(
                    cat_edit.model_dump(exclude_unset=True)
                )
            )

            await session.execute(stmt)
            await session.commit()

            return {"status": "success"}

    @staticmethod
    async def delete_cat(
        cat_id:int
):
        async with async_session_maker() as session:
            stmt = (
                delete(Cat).
                where(Cat.id==cat_id)
            )

            await session.execute(stmt)
            await session.commit()

            return {"status": "success"}

class BreedRepository:

    @staticmethod
    async def create_breed(
        new_breed_model:Create_breed_model,
) -> Breed:
        async with async_session_maker() as session:
            stmt = Breed(**new_breed_model.model_dump())
            session.add(stmt)
            await session.commit()

            return stmt
        
    @staticmethod
    async def get_all_breeds() -> list[Breed]:
        async with async_session_maker() as session:
            query = (
                select(Breed).
                order_by(Breed.id)
            )

            all_breeds = await session.scalars(query)
            
            return list(all_breeds)
        
    @staticmethod
    async def edit_breed(
        breed_id:int,
        breed_edit:Edit_breed_model
):
        async with async_session_maker() as session:
            stmt = (
                update(Breed).
                where(Breed.id==breed_id).
                values(
                    breed_edit.model_dump()
                )
            )

            await session.execute(stmt)
            await session.commit()

            return {"status": "success"}
        
    @staticmethod
    async def delete_breed(
        breed_id:int
):
        async with async_session_maker() as session:
            stmt = (
                delete(Breed).
                where(Breed.id==breed_id)
            )
            await session.execute(stmt)
            await session.commit()

            return {"status": "success"}
