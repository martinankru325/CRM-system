from django.urls import path
from .views import UserLoginView, UserLogoutView, index

app_name = 'users'

urlpatterns = [
    path('', index, name='index'),  # например, корень users/
    path('users/login/', UserLoginView.as_view(), name='login'),
    path('users/logout/', UserLogoutView.as_view(), name='logout'),
]
