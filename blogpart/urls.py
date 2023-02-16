from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='blog_detail')
]
