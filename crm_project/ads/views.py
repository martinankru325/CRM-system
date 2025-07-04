from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Count, Sum, F, ExpressionWrapper, FloatField, Case, When, Value

from .models import Ad
from .forms import AdForm


class AdListView(LoginRequiredMixin, ListView):
    model = Ad
    template_name = 'ads/ads-list.html'
    context_object_name = 'ads'


class AdDetailView(LoginRequiredMixin, DetailView):
    model = Ad
    template_name = 'ads/ads-detail.html'
    context_object_name = 'ad'


class AdCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Ad
    form_class = AdForm
    template_name = 'ads/ads-create.html'
    success_url = reverse_lazy('ads:ads-list')
    permission_required = 'crm_app.add_ad'


class AdUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Ad
    form_class = AdForm
    template_name = 'ads/ads-edit.html'
    success_url = reverse_lazy('ads:ads-list')  # исправлено
    permission_required = 'crm_app.change_ad'


class AdDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Ad
    template_name = 'ads/ads-delete.html'
    success_url = reverse_lazy('ads:ads-list')  # исправлено
    permission_required = 'crm_app.delete_ad'


@login_required
def ads_statistic(request):
    ads = Ad.objects.annotate(
        leads_count=Count('leads'),
        customers_count=Count('leads__customers'),
        total_contract_amount=Sum('leads__customers__contract__amount'),
    ).annotate(
        roi=Case(
            When(budget=0, then=Value(0.0)),
            default=ExpressionWrapper(
                F('total_contract_amount') / F('budget'),
                output_field=FloatField()
            )
        )
    )
    return render(request, 'ads/ads-statistic.html', {'ads': ads})
