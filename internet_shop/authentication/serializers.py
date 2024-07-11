from .models import Users
from database import session_maker

import hashlib

from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)
    role = serializers.IntegerField(read_only=True, default=6)

    def verify_email(self, value) -> str:
        session = session_maker()
        if session.query(Users).filter_by(email=value).first():
            session.close()
            raise serializers.ValidationError("Данный email уже существует")
        session.close()
        return value

    def create(self, validated_data):
        session = session_maker()
        email = self.verify_email(validated_data["email"])
        password = validated_data["password"]
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        user = Users(email=email, hashed_password=hashed_password, role=6)
        session.add(user)
        session.commit()
        session.close()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)

    def validate(self, data):
        session = session_maker()
        email = data["email"]
        password = data["password"]
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        user = session.query(Users).filter_by(email=email, hashed_password=hashed_password).first()
        session.close()
        if not user:
            raise serializers.ValidationError("Неверные данные для входа")
        return data


class UsersSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=100)
    hashed_password = serializers.CharField(max_length=300)
    role = serializers.IntegerField()


class UsersPasswordUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    hashed_password = serializers.CharField(max_length=300)
