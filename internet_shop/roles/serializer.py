from rest_framework import serializers


class RolesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    role_name = serializers.CharField(max_length=100)

