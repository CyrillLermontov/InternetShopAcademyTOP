from rest_framework import serializers


class CategoriesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category_name = serializers.CharField(max_length=100)

