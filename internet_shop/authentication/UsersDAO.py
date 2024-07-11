from sqlalchemy import select

from base.BaseDAO import BaseDAO
from .models import Users
from database import session_maker


class UsersDAO(BaseDAO):
    @classmethod
    def find_by_email(cls, email: str) -> list:
        with session_maker() as session:
            query = select(Users).where(Users.\
                                             email.ilike(f"%{email}%"))
            result = session.execute(query)
            return [row for row in result.scalars()]
