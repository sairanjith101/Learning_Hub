from rest_framework import serializers
from orders.models import Order, OrderItem, Payment
from products.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'price')

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'total', 'status', 'created_at', 'items')
        read_only_fields = ('id', 'user', 'total', 'created_at', 'items')

class PaymentSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.Objects.all())

    class Meta:
        model = Payment
        fields = ('id', 'order', 'amount', 'method', 'transaction_id', 'success', 'created_at')
        read_only_fields = ('id', 'created_at')