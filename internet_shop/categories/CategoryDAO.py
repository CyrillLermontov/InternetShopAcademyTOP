from sqlalchemy import select

from base.BaseDAO import BaseDAO
from .models import Categories
from database import session_maker


class CategoryDAO(BaseDAO):
    @classmethod
    def find_by_name(cls, category_name: str) -> list:
        with session_maker() as session:
            query = select(Categories).where(Categories.\
                                             category_name.ilike(f"%{category_name}%"))
            result = session.execute(query)
            return [row for row in result.scalars()]