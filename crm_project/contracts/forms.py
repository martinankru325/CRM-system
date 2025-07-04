from django import forms
from .models import Contract


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['name', 'product', 'document', 'date_signed', 'duration_months', 'amount']