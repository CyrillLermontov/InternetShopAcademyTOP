from .models import Products

from rest_framework import serializers


class ProductsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    product_name = serializers.CharField(max_length=100)
    category = serializers.IntegerField()
    description = serializers.CharField(max_length=1000)
    cost = serializers.FloatField()
    count_of_sells = serializers.IntegerField()
    discount = serializers.FloatField()

    def create(self, validated_data):
        return Products(**validated_data)

    def update(self, instance, validated_data):
        instance.product_name = validated_data.get('product_name', instance.product_name)
        instance.category = validated_data.get('category', instance.category)
        instance.description = validated_data.get('description', instance.description)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.count_of_sells = validated_data.get('count_of_sells', instance.count_of_sells)
        instance.discount = validated_data.get('discount', instance.discount)
        return instance

