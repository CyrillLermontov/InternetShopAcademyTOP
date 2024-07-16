from sqlalchemy import select, join

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
        users = cls.find_all(Users)
        roles = cls.find_all(Roles)
        roles_dict = {}
        for role in roles:
            roles_dict[role.id] = role.role_name
        result = []
        for u in users:
            info = {
                'id': u.id,
                'email': u.email,
                'hashed_password': u.hashed_password,
                'role': roles_dict[u.role],
            }
            result.append(info)
        return result
    
    @classmethod
    def find_user_by_id(cls, id: int) -> list:
        users = cls.find_by_id(Users, id)
        if not users:
            return None
        roles = cls.find_all(Roles)
        roles_dict = {}
        for role in roles:
            roles_dict[role.id] = role.role_name
        result = []
        for u in users:
            info = {
                'id': u.id,
                'email': u.email,
                'hashed_password': u.hashed_password,
                'role': roles_dict[u.role],
            }
            result.append(info)
        return result


