from rest_framework import serializers
from .models import Order, OrderProduct
from product.models import Product


class OrderProductSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity = serializers.IntegerField()


class CreateOrderSerializer(serializers.Serializer):
    products = serializers.ListField(child=OrderProductSerializer())


class OrderSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user_id.username")

    class Meta:
        model = Order
        fields = ["username", "total_sum", "delivered"]


class SubtractProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["quantity"]
