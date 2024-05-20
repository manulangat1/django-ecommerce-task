from rest_framework import serializers
from apps.products.serializers import ProductSerializer
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):

    item = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ("id", "item", "quantity")

    def get_item(self, obj):
        return ProductSerializer(obj.item).data


class OrderSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ("id", "ordered", "order_items", "total_price")

    def get_order_items(self, obj):
        return OrderItemSerializer(obj.orderItems, many=True).data

    def get_total_price(self, obj):
        return obj.get_total_price()
