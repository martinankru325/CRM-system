from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from ads.models import Ad
from leads.models import Lead
from customers.models import Customer

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True  # если уже залогинен, перенаправит

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')  # после выхода — на страницу логина

def home(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('users:login')


@login_required
def index(request):
    context = {
        'products_count': Product.objects.count(),
        'advertisements_count': Ad.objects.count(),
        'leads_count': Lead.objects.count(),
        'customers_count': Customer.objects.count(),
    }
    return render(request, 'index.html', context)
