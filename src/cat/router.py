from typing import Annotated

from fastapi import APIRouter, Body, Query

from src.cat.schemas import (
    Create_cat_model,
    Edit_cat_model,
    Create_breed_model,
    Edit_breed_model
)

from src.cat.crud import (
    CatRepository, 
    BreedRepository
)


router = APIRouter(
    prefix="/Cat",
    tags= ["Cat"]
)

# Роутеры для модели кошек

@router.post("/add_cat")
async def add_cat(new_cat_model:Annotated[Create_cat_model, Body()],
):
    stmt = await CatRepository.create_cat(new_cat_model=new_cat_model)
    return stmt

@router.get("/get_all_cats")
async def get_all_cats():
    query = await CatRepository.get_all_cats()
    return query

@router.get("/get_cat_by_id")
async def get_cat_by_id(cat_id:Annotated[int, Query()]):
    query = await CatRepository.get_cat_by_id(cat_id=cat_id)
    return query

@router.get("/get_cats_by_breed")
async def get_cats_by_breed(breed_id:Annotated[int, Query]):
    query = await CatRepository.get_cats_by_breed(breed_id=breed_id)
    return query

@router.patch("/edit_cat")
async def edit_cat(cat_edit:Annotated[Edit_cat_model, Body()], cat_id:Annotated[int, Query()]):
    stmt = await CatRepository.edit_cat(cat_edit=cat_edit, cat_id=cat_id)
    return stmt

@router.delete("/detele_cat/{cat_id}")
async def delete_cat(cat_id:int):
    stmt = await CatRepository.delete_cat(cat_id=cat_id)
    return stmt


# Роутеры для модели пород

@router.post("/add_breed")
async def add_bread(new_breed_model:Annotated[Create_breed_model, Body()]

):
    stmt = await BreedRepository.create_breed(new_breed_model=new_breed_model)
    return stmt

@router.get("/get_all_breeds")
async def get_all_breeds():
    query = await BreedRepository.get_all_breeds()
    return query

@router.put("/edit_breed")
async def edit_breed(breed_edit: Annotated[Edit_breed_model, Body()], breed_id:Annotated[int, Query()]):
    stmt = await BreedRepository.edit_breed(breed_edit=breed_edit, breed_id=breed_id)
    return stmt

@router.delete("/delete_breed")
async def delete_breed(breed_id:Annotated[int, Query()]):
    stmt = await BreedRepository.delete_breed(breed_id=breed_id)
    return stmt