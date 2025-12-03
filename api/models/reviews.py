from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime, UTC
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), index=True, nullable=False)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"), index=True, nullable=True)
    order_id = Column(Integer, ForeignKey("orders.id"), index=True, nullable=True)

    rating = Column(Integer, nullable=False)  # 1..5
    text = Column(String(1000), nullable=True)
    created_at = Column(DateTime, nullable=False, default=lambda: datetime.now(UTC))
