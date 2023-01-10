from rest_framework import serializers
from core.models import Order
from sandwiches.models import Sandwich

class SandwichSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sandwich
        fields = ['name', 'slug', 'id']

class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    order_date = serializers.DateTimeField(read_only=True)
    sandwich = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        queryset=Sandwich.objects.all(),
        required=True
    )

    class Meta:
        model = Order
        fields = ['id', 'owner', 'email', 'sandwich', 'bread_type', 'order_date']
