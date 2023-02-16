from django.contrib import admin
from django.urls import path, include
from .views import ContactCreate, success

urlpatterns = [
    path('', ContactCreate.as_view(), name='contact_page'),
    path('success/', success, name='success_page')
    ]
