from sqlalchemy import Column, Integer, String, Numeric, Boolean, DateTime
from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, index=True, nullable=False)
    description = Column(String(255), nullable=True)

    # Use either percent or amount. Keep both optional so you can support either style.
    discount_percent = Column(Numeric(5, 2), nullable=True)  # 0..100
    discount_amount  = Column(Numeric(10, 2), nullable=True) # flat amount

    expires_at = Column(DateTime, nullable=True)
    active = Column(Boolean, default=True, nullable=False)