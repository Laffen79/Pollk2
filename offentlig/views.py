from django.shortcuts import render, redirect
from django.contrib.auth import logout


# Create your views here.
def home(request):
    return render(request, 'offentlig/home.html')

def about(request):
    return render(request, 'offentlig/about.html')

def products(request):
    return render(request, 'offentlig/products.html')

def contact(request):
    return render(request, 'offentlig/contact.html')

def dealers(request):
    return render(request, 'offentlig/dealers.html')

def logg_ut(request):
    logout(request)
    return redirect('home')

def logg_inn(request):
    logout(request)
    return redirect('admin/')