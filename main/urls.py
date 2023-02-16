from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    # path('blog', views.blog, name='blog'),
    path('inspiration', views.inspiration, name='inspiration'),
    path('about', views.about, name='about'),
    # path('connect', views.connect, name='connect')
]

