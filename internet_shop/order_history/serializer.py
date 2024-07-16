from rest_framework import serializers


class OrderHistorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    product = serializers.CharField(max_length=100)
    date = serializers.DateField()
    quantity = serializers.IntegerField()
    full_cost = serializers.FloatField()
    client = serializers.IntegerField()

