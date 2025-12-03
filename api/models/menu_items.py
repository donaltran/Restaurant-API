from sqlalchemy import Column, Integer, String, Numeric
from ..dependencies.database import Base


class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False, index=True)
    description = Column(String(500), nullable=True)
    price = Column(Numeric(10, 2), nullable=False)
    calories = Column(Integer, nullable=True)
    category = Column(String(80), nullable=True)