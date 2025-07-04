from django.db import models
from django.contrib.auth.models import User
from leads.models import Lead
from contracts.models import Contract

class Customer(models.Model):
    lead = models.OneToOneField(Lead, on_delete=models.CASCADE, related_name='customers')
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, related_name='customers')

    def __str__(self):
        return f"{self.lead.full_name} - {self.contract.name}"

