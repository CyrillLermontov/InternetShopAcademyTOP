from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import datetime
import jwt
import hashlib

from base.responses import SuccessPutResponse, BadPutResponse, SuccessGetResponse, \
    BadGetResponse
from .serializers import RegisterSerializer, LoginSerializer, UsersSerializer, \
    UsersPasswordUpdateSerializer
from .models import Users
from database import session_maker
from authentication.dependencies import role_required
from base.BaseViewSet import BaseViewSet
from .UsersDAO import UsersDAO


class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"status": "success", "msg": "Регистрация прошла успешно"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST,)


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        if request.COOKIES.get('access_token'):
            return Response(data={'message': 'Вы уже авторизованы'},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data["email"]
            session = session_maker()
            user = session.query(Users).filter_by(email=email).first()  # Получаем пользователя снова
            session.close()

            payload = {
                "id": user.id,
                "exp": datetime.datetime.now() + datetime.timedelta(hours=1),
            }
            token = jwt.encode(payload, 'secret', algorithm="HS256")
            response = Response({"message": "Вход выполнен успешно", "token": token}, status=status.HTTP_202_ACCEPTED)
            response.set_cookie(key='access_token', value=token, httponly=True)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        if request.COOKIES.get('access_token'):
            response.delete_cookie('access_token')
            response.data = {'message': 'Выход выполнен успешно'}
            return response
        response.status_code = status.HTTP_401_UNAUTHORIZED
        response.data = {'message': 'Вы не авторизованы'}
        return response


class UserPasswordUpdateView(APIView):
    serializer_class = UsersPasswordUpdateSerializer

    @role_required(5, 6)
    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        result = UsersDAO.find_by_id(Users, pk)
        if result is None:
            return BadPutResponse(data=[])
        hashed_password = hashlib.md5(request.data["password"].encode()).hexdigest()
        result = UsersDAO.update(Users, pk, {"hashed_password": hashed_password})
        serializer = self.serializer_class(result)
        return SuccessPutResponse(data=serializer.data)


class UsersView(APIView):
    serializer_class = UsersSerializer

    @role_required(5)
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        if pk is None:
            users = UsersDAO.find_all(Users)
            serializer = self.serializer_class(users, many=True)
            return SuccessGetResponse(data=serializer.data)
        else:
            result = UsersDAO.find_by_id(Users, pk)
            if result is None:
                return BadGetResponse(data=[])
            serializer = self.serializer_class(result[0])
            return SuccessGetResponse(data=serializer.data)

