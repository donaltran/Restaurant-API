from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..controllers import promotions as controller
from ..schemas import promotions as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Sandwiches'],
    prefix="/sandwiches"
)


@router.post("/", response_model=schema.Sandwich, status_code=status.HTTP_201_CREATED)
def create_sandwich(request: schema.SandwichCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Sandwich])
def read_all_sandwiches(db: Session = Depends(get_db)):
    return controller.read_all(db=db)


@router.get("/{item_id}", response_model=schema.Sandwich)
def read_sandwich(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db=db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.Sandwich)
def update_sandwich(item_id: int, request: schema.SandwichUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, item_id=item_id, request=request)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sandwich(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)