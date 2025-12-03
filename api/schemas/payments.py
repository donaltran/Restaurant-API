from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PaymentBase(BaseModel):
    order_id: int
    customer_id: int
    amount: float
    method: str
    status: Optional[str] = "APPROVED"
    transaction_id: Optional[str] = None


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    # fields that are realistically updated after creation
    method: Optional[str] = None
    status: Optional[str] = None
    transaction_id: Optional[str] = None


class Payment(PaymentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True