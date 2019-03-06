from django.urls import path

# views
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about')
]