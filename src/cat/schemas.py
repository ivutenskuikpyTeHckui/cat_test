from typing import Optional

from pydantic import BaseModel


# Схемы для кошек(модель Cat)

class Create_cat_model(BaseModel):

    color: str
    age: int
    description: str 
    breed_id: int

class Edit_cat_model(BaseModel):

    color: Optional[str] = None 
    age: Optional[int] = None
    description: Optional[str] = None
    breed_id: Optional[int] = None


# Схемы для пород(модель Breed) кошек

class Create_breed_model(BaseModel):

    name: str

class Edit_breed_model(BaseModel):

    name: str