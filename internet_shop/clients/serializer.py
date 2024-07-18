from rest_framework import serializers


class ClientSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=100)

