from django.db import models
from authentication.models import User
from product.models import Product


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total_sum = models.IntegerField(null=True)
    delivered = models.BooleanField(default=False)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)


class OrderProduct(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, default=None)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.IntegerField(null=True, blank=True)
