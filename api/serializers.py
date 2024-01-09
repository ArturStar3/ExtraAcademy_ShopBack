from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    quantity = serializers.IntegerField(allow_null=True)
    category_id = serializers.IntegerField()


