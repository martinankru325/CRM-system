from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Lead
from customers.models import Customer
from contracts.forms import ContractForm
from .forms import LeadForm


class LeadListView(LoginRequiredMixin, ListView):
    model = Lead
    template_name = 'leads/leads-list.html'
    context_object_name = 'leads'  # множественное число


class LeadDetailView(LoginRequiredMixin, DetailView):
    model = Lead
    template_name = 'leads/leads-detail.html'
    context_object_name = 'lead'


class LeadCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Lead
    form_class = LeadForm
    template_name = 'leads/leads-create.html'
    success_url = reverse_lazy('leads:leads-list')
    permission_required = 'crm_app.add_lead'


class LeadUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Lead
    form_class = LeadForm
    template_name = 'leads/leads-edit.html'
    success_url = reverse_lazy('leads:leads-list')
    permission_required = 'crm_app.change_lead'  # исправлено


class LeadDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Lead
    template_name = 'leads/leads-delete.html'
    success_url = reverse_lazy('leads:leads-list')
    permission_required = 'crm_app.delete_lead'


@login_required
def convert_lead_to_customer(request, lead_id):
    lead = get_object_or_404(Lead, pk=lead_id)

    # Проверяем, есть ли уже клиент для этого лида
    if Customer.objects.filter(lead=lead).exists():
        messages.warning(request, 'Этот лид уже конвертирован в клиента.')
        return redirect('customers:customers-detail', pk=Customer.objects.get(lead=lead).pk)

    if request.method == 'POST':
        contract_form = ContractForm(request.POST, request.FILES)
        if contract_form.is_valid():
            with transaction.atomic():
                contract = contract_form.save()
                customer = Customer.objects.create(lead=lead, contract=contract)
            messages.success(request, 'Лид успешно конвертирован в клиента.')
            return redirect('customers:customers-detail', pk=customer.pk)
    else:
        contract_form = ContractForm()

    return render(request, 'leads/convert_lead.html', {'lead': lead, 'contract_form': contract_form})

