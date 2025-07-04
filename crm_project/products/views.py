from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Product
from .forms import ProductForm


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/products-list.html'
    context_object_name = 'products'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'products/products-detail.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/products-create.html'
    success_url = reverse_lazy('products:products-list')
    permission_required = 'crm_app.add_product'


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/products-edit.html'
    permission_required = 'crm_app.change_product'

    def get_success_url(self):
        # Возвращаем URL страницы деталей для отредактированного объекта
        return reverse('products:products-detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/products-delete.html'
    success_url = reverse_lazy('products:products-list')
    permission_required = 'crm_app.delete_product'

