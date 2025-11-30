from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..dependencies.database import get_db
from ..schemas import menu_items as schema
from ..controllers import menu_items as controller

router = APIRouter(
    prefix="/menu_items",
    tags=["Menu Items"],
)


@router.post(
    "/",
    response_model=schema.MenuItem,
    status_code=status.HTTP_201_CREATED,
)
def create_menu_item(
    request: schema.MenuItemCreate,
    db: Session = Depends(get_db),
):
    return controller.create(db, request)


@router.get(
    "/",
    response_model=list[schema.MenuItem],
)
def read_menu_items(
    db: Session = Depends(get_db),
):
    return controller.read_all(db)


@router.get(
    "/{item_id}",
    response_model=schema.MenuItem,
)
def read_menu_item(
    item_id: int,
    db: Session = Depends(get_db),
):
    return controller.read_one(db, item_id)


@router.put(
    "/{item_id}",
    response_model=schema.MenuItem,
)
def update_menu_item(
    item_id: int,
    request: schema.MenuItemUpdate,
    db: Session = Depends(get_db),
):
    return controller.update(db, item_id, request)


@router.delete(
    "/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_menu_item(
    item_id: int,
    db: Session = Depends(get_db),
):
    return controller.delete(db, item_id)