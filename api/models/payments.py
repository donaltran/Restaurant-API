from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from datetime import datetime
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), index=True, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), index=True, nullable=False)

    amount = Column(Numeric(10, 2), nullable=False)
    method = Column(String(30), nullable=False)       # e.g., CARD, CASH, APPLE_PAY
    status = Column(String(30), nullable=False, default="APPROVED")  # PENDING/APPROVED/DECLINED/REFUNDED
    transaction_id = Column(String(120), nullable=True, index=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)