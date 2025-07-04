from django.urls import path
from . import views

app_name = "ads"

urlpatterns = [
    path('', views.AdListView.as_view(), name='ads-list'),
    path('create/', views.AdCreateView.as_view(), name='ads-create'),
    path('<int:pk>/', views.AdDetailView.as_view(), name='ads-detail'),
    path('<int:pk>/edit/', views.AdUpdateView.as_view(), name='ads-edit'),
    path('<int:pk>/delete/', views.AdDeleteView.as_view(), name='ads-delete'),
    path('statistic/', views.ads_statistic, name='ads-statistic'),
    ]