from database import session_maker
import hashlib


from internet_shop.authentication.models import Users
from internet_shop.roles.models import Roles


def reg_us():
    email = input()
    password = input()
    role = int(input())
    session = session_maker()
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    user = Users(email=email, hashed_password=hashed_password, role=role)
    session.add(user)
    session.commit()
    session.close()


reg_us()