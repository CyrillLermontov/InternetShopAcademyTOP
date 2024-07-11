from .models import Client

from rest_framework import serializers


class ClientSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Client(**validated_data)

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        return instance

