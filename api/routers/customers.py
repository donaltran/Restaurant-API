from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..schemas import customers as schema
from ..controllers import customers as controller

router = APIRouter(
    prefix="/customers",
    tags=["Customers"],
)


@router.post("/", response_model=schema.Customer, status_code=status.HTTP_201_CREATED)
def create_customer(
    request: schema.CustomerCreate,
    db: Session = Depends(get_db),
):
    return controller.create(db, request)


@router.get("/", response_model=list[schema.Customer])
def read_customers(
    db: Session = Depends(get_db),
):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.Customer)
def read_customer(
    item_id: int,
    db: Session = Depends(get_db),
):
    return controller.read_one(db, item_id)


@router.put("/{item_id}", response_model=schema.Customer)
def update_customer(
    item_id: int,
    request: schema.CustomerUpdate,
    db: Session = Depends(get_db),
):
    return controller.update(db, item_id, request)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(
    item_id: int,
    db: Session = Depends(get_db),
):
    return controller.delete(db, item_id)