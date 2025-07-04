from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products-list'),
    path('create/', views.ProductCreateView.as_view(), name='products-create'),
    path('<int:pk>', views.ProductDetailView.as_view(), name='products-detail'),
    path('<int:pk>/edit/', views.ProductUpdateView.as_view(), name='products-edit'),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view(), name='products-delete'),
    ]