from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..dependencies.database import get_db
from ..schemas import recipes as schema
from ..controllers import recipes as controller

router = APIRouter(
    prefix="/recipes",
    tags=["Recipes"],
)


@router.post(
    "/",
    response_model=schema.Recipe,
    status_code=status.HTTP_201_CREATED,
)
def create_recipe(
    request: schema.RecipeCreate,
    db: Session = Depends(get_db),
):
    return controller.create(db, request)


@router.get(
    "/",
    response_model=list[schema.Recipe],
)
def read_recipes(
    db: Session = Depends(get_db),
):
    return controller.read_all(db)


@router.get(
    "/{item_id}",
    response_model=schema.Recipe,
)
def read_recipe(
    item_id: int,
    db: Session = Depends(get_db),
):
    return controller.read_one(db, item_id)


@router.put(
    "/{item_id}",
    response_model=schema.Recipe,
)
def update_recipe(
    item_id: int,
    request: schema.RecipeUpdate,
    db: Session = Depends(get_db),
):
    return controller.update(db, item_id, request)


@router.delete(
    "/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_recipe(
    item_id: int,
    db: Session = Depends(get_db),
):
    return controller.delete(db, item_id)