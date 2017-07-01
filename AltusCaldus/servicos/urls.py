from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'aula/', views.aula),
    url(r'guarderia/', views.guarderia),
    url(r'aluguel/', views.aluguel),
]
