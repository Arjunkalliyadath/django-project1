from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'About.html')

def contact(request):
    return render(request, 'Contact.html')

def form_view(request):
    return render(request, 'form.html')

def login(request):
    return render(request, 'Login.html')

def register(request):
    return render(request, 'Register.html')

def home_page(request):
    return render(request, 'Home.html')
