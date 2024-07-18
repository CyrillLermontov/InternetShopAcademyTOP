from rest_framework import serializers


class ProductsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    product_name = serializers.CharField(max_length=100)
    category = serializers.IntegerField()
    description = serializers.CharField(max_length=1000)
    cost = serializers.FloatField()
    count_of_sells = serializers.IntegerField()
    discount = serializers.FloatField()

