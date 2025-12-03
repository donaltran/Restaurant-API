from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..dependencies.database import get_db
from ..schemas import sandwiches as schema
from ..controllers import sandwiches as controller

router = APIRouter(
    prefix="/sandwiches",
    tags=["Sandwiches"],
)


@router.post(
    "/",
    response_model=schema.Sandwich,
    status_code=status.HTTP_201_CREATED,
)
def create_sandwich(
    request: schema.SandwichCreate,
    db: Session = Depends(get_db),
):
    return controller.create(db, request)


@router.get(
    "/",
    response_model=list[schema.Sandwich],
)
def read_sandwiches(
    db: Session = Depends(get_db),
):
    return controller.read_all(db)


@router.get(
    "/{item_id}",
    response_model=schema.Sandwich,
)
def read_sandwich(
    item_id: int,
    db: Session = Depends(get_db),
):
    return controller.read_one(db, item_id)


@router.put(
    "/{item_id}",
    response_model=schema.Sandwich,
)
def update_sandwich(
    item_id: int,
    request: schema.SandwichUpdate,
    db: Session = Depends(get_db),
):
    return controller.update(db, item_id, request)


@router.delete(
    "/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_sandwich(
    item_id: int,
    db: Session = Depends(get_db),
):
    return controller.delete(db, item_id)