from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PromotionBase(BaseModel):
    code: str
    description: Optional[str] = None
    discount_percent: Optional[float] = None
    discount_amount: Optional[float] = None
    expires_at: Optional[datetime] = None
    active: bool = True


class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    description: Optional[str] = None
    discount_percent: Optional[float] = None
    discount_amount: Optional[float] = None
    expires_at: Optional[datetime] = None
    active: Optional[bool] = None


class Promotion(PromotionBase):
    id: int

    class Config:
        orm_mode = True