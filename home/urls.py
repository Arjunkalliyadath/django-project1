from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('form/', views.form_view, name='form'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home_page, name='home_page'),
]
