from django.conf.urls import include, url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^$', views.index),
    url(r'aula/', views.aula, name='aula'),
    url(r'guarderia/', views.guarderia, name='guarderia'),
    url(r'aluguel/', views.aluguel, name='aluguel'),
]
