from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSeriaizer
from rest_framework.response import Response


class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSeriaizer
        return Response(serializer(products, many=True).data)

    def post(self, request):
        serializer = ProductSeriaizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def put(self, request, *arks, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"method": "method PUT not allowed"})
        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({"method": "Object does not exist"})

        serializer = ProductSeriaizer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"method": "method DELETE not allowed"})
        to_delete = Product.objects.get(id=pk)
        to_delete.delete()
        return Response(f"success")



