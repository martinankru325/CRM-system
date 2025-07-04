from django.urls import path
from . import views

app_name = "contracts"

urlpatterns = [
    path('', views.ContractListView.as_view(), name='contracts-list'),
    path('create/', views.ContractCreateView.as_view(), name='contracts-create'),
    path('<int:pk>/', views.ContractDetailView.as_view(), name='contracts-detail'),
    path('<int:pk>/edit/', views.ContractUpdateView.as_view(), name='contracts-edit'),
    path('<int:pk>/delete/', views.ContractDeleteView.as_view(), name='contracts-delete'),
]