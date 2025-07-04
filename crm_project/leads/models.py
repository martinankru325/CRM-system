from django.db import models
from django.contrib.auth.models import User

from ads.models import Ad


class Lead(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    ads = models.ForeignKey(Ad, on_delete=models.SET_NULL, null=True, related_name='leads')

    def __str__(self):
        return self.full_name

