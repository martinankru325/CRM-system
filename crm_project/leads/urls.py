from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    path('', views.LeadListView.as_view(), name='leads-list'),
    path('create/', views.LeadCreateView.as_view(), name='leads-create'),
    path('<int:pk>/', views.LeadDetailView.as_view(), name='leads-detail'),
    path('<int:pk>/edit/', views.LeadUpdateView.as_view(), name='leads-edit'),
    path('<int:pk>/delete/', views.LeadDeleteView.as_view(), name='leads-delete'),
    path('<int:lead_id>/convert/', views.convert_lead_to_customer, name='convert-lead-to-customer'),
    ]