from rest_framework import serializers
from core.models import Order

class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    order_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'owner', 'email', 'sandwich', 'bread_type', 'order_date']
