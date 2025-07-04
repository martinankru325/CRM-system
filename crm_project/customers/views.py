from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Customer
from .forms import CustomerForm


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customers/customers-list.html'
    context_object_name = 'customers'


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'customers/customers-detail.html'
    context_object_name = 'customer'


class CustomerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customers-create.html'
    success_url = reverse_lazy('customers:customers-list')
    permission_required = 'crm_app.add_customer'


class CustomerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customers-edit.html'
    success_url = reverse_lazy('customers:customers-list')
    permission_required = 'crm_app.change_customer'


class CustomerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customers-delete.html'
    success_url = reverse_lazy('customers:customers-list')
    permission_required = 'crm_app.delete_customer'
