from django.conf.urls import include, url
from loja import views
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.loja_online),
    url(r'servicos/', include('servicos.urls')),
]