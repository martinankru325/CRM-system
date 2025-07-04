from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Contract
from .forms import ContractForm


class ContractListView(LoginRequiredMixin, ListView):
    model = Contract
    template_name = 'contracts/contracts-list.html'
    context_object_name = 'contracts'


class ContractDetailView(LoginRequiredMixin, DetailView):
    model = Contract
    template_name = 'contracts/contracts-detail.html'
    context_object_name = 'contract'  # исправлено


class ContractCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Contract
    form_class = ContractForm
    template_name = 'contracts/contracts-create.html'
    success_url = reverse_lazy('contracts:contracts-list')
    permission_required = 'crm_app.add_contract'


class ContractUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Contract
    form_class = ContractForm
    template_name = 'contracts/contracts-edit.html'
    success_url = reverse_lazy('contracts:contracts-list')  # исправлено
    permission_required = 'crm_app.change_contract'


class ContractDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Contract
    template_name = 'contracts/contracts-delete.html'
    success_url = reverse_lazy('contracts:contracts-list')  # исправлено
    permission_required = 'crm_app.delete_contract'
