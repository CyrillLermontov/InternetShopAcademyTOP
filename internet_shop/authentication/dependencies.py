from rest_framework.response import Response
from rest_framework import status

import jwt
from functools import wraps

from .models import Users
from database import session_maker


def get_user_from_token(request):
    token = request.COOKIES.get('access_token')
    if not token:
        return None
    try:
        payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        session = session_maker()
        user = session.query(Users).filter_by(id=payload["id"]).first()
        session.close()
        if not user:
            return None
        return user
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None


def role_required(*roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(view, request, *args, **kwargs):
            user = get_user_from_token(request)
            if not user or user.role not in roles:
                return Response({'detail': 'У вас нет доступа к этому ресурсу'},
                                status=status.HTTP_403_FORBIDDEN)
            return view_func(view, request, *args, **kwargs)
        return wrapper
    return decorator