from rest_framework import serializers
from .models import Product, Category


class ProductSeriaizer(serializers.ModelSerializer):
    category_id = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = Product
        fields = ["name", "description", "price", "quantity", "category_id", "image"]


