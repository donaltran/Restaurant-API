from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..dependencies.database import get_db
from ..schemas import reviews as schema
from ..controllers import reviews as controller

router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"],
)


@router.post(
    "/",
    response_model=schema.Review,
    status_code=status.HTTP_201_CREATED,
)
def create_review(
    request: schema.ReviewCreate,
    db: Session = Depends(get_db),
):
    return controller.create(db, request)


@router.get(
    "/",
    response_model=list[schema.Review],
)
def read_reviews(
    db: Session = Depends(get_db),
):
    return controller.read_all(db)


@router.get(
    "/{item_id}",
    response_model=schema.Review,
)
def read_review(
    item_id: int,
    db: Session = Depends(get_db),
):
    return controller.read_one(db, item_id)


@router.put(
    "/{item_id}",
    response_model=schema.Review,
)
def update_review(
    item_id: int,
    request: schema.ReviewCreate,
    db: Session = Depends(get_db),
):
    return controller.update(db, item_id, request)


@router.delete(
    "/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_review(
    item_id: int,
    db: Session = Depends(get_db),
):
    return controller.delete(db, item_id)