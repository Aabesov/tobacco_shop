from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from product.models import Product
from .models import Order, OrderProduct
from .serializers import CreateOrderSerializer, OrderSerializer, SubtractProductSerializer


class CreateOrderAPIView(APIView):

    def put(self):
        pass

    def post(self, request, *args, **kwargs):
        serializer = CreateOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        products = serializer.validated_data.get("products")
        order_price = 0

        order = Order.objects.create(user_id=request.user)

        for i in products:
            quantity = i.get("quantity")
            product = i.get('product')
            total_price = product.price * quantity
            data = dict(order_id=order, product_id=i.get("product"), quantity=i.get("quantity"),
                        total_price=total_price)
            OrderProduct.objects.create(**data)
            order_price += total_price
        order.total_sum = order_price
        order.save()
        order_serializer = OrderSerializer(instance=order)
        return Response(order_serializer.data)
