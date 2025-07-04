from django.urls import path
from . import views

app_name = "customers"

urlpatterns = [
    path('', views.CustomerListView.as_view(), name='customers-list'),
    path('create/', views.CustomerCreateView.as_view(), name='customers-create'),
    path('<int:pk>/', views.CustomerDetailView.as_view(), name='customers-detail'),
    path('<int:pk>/edit/', views.CustomerUpdateView.as_view(), name='customers-edit'),
    path('<int:pk>/delete/', views.CustomerDeleteView.as_view(), name='customers-delete'),
    ]