from sqlalchemy import Column, Integer, String

from database import Base


class Categories(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    category_name = Column(String(50), nullable=False)