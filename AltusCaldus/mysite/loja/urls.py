from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.list_produto),
    url(r'^index', views.template),
]