from django.db import models
from products.models import Product

class Contract(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='contracts')
    document = models.FileField(upload_to='contracts/')
    date_signed = models.DateField()
    duration_months = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name
