from django.db import models
from products.models import Product

class Ad(models.Model):
    name = models.CharField(max_length=255, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ad')
    channel = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name
