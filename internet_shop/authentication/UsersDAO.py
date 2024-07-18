from sqlalchemy import select
from sqlalchemy.orm import aliased

from base.BaseDAO import BaseDAO
from .models import Users
from roles.models import Roles
from database import session_maker


class UsersDAO(BaseDAO):
    @classmethod
    def find_by_email(cls, email: str) -> list:
        with session_maker() as session:
            query = select(Users).where(Users.\
                                             email.ilike(f"%{email}%"))
            result = session.execute(query)
            return [row for row in result.scalars()]
        

    @classmethod
    def find_all_users(cls) -> list:
        with session_maker() as session:
            roles_alias = aliased(Roles)
            query = (
            select(
                Users.id,
                Users.email,
                Users.hashed_password,
                roles_alias.role_name,
            )
            .select_from(Users)
            .join(roles_alias, Users.role == roles_alias.id)
            )
            result = []
            for row in session.execute(query):
                info = {
                    'id': row.id,
                    'email': row.email,
                    'hashed_password': row.hashed_password,
                    'role': row.role_name,
                }
                result.append(info)
        return result
    
    
    @classmethod
    def find_user_by_id(cls, id: int) -> list:
        with session_maker() as session:
            roles_alias = aliased(Roles)
            query = (
            select(
                Users.id,
                Users.email,
                Users.hashed_password,
                roles_alias.role_name,
            )
            .select_from(Users)
            .join(roles_alias, Users.role == roles_alias.id)
            .where(Users.id == id)
            )
            result = []
            for row in session.execute(query):
                info = {
                    'id': row.id,
                    'email': row.email,
                    'hashed_password': row.hashed_password,
                    'role': row.role_name,
                }
                result.append(info)
        return result


