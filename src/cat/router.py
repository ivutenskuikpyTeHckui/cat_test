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

@router.post("/add_cat")
async def add_cat(new_cat_model:Annotated[Create_cat_model, Body()],
):
    new_cat = await CatRepository.create_cat(new_cat_model)
    return new_cat

@router.get("/get_all_cats")
async def get_all_cats():
    all_cats = await CatRepository.get_all_cats()
    return all_cats

@router.post("/add_breed")
async def add_bread(new_breed_model:Annotated[Create_breed_model, Body()]

):
    new_breed = await BreedRepository.create_breed(new_breed_model)
    return new_breed