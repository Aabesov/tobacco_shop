from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.name


class Product(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    price = models.PositiveSmallIntegerField()
    quantity = models.PositiveSmallIntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    image = models.ImageField(null=False)

    # def __str__(self):
    #     return self.name
