"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from aparcamientos import views
from django.views.static import *
from myproject import settings

urlpatterns = [
    url(r'^main.css/', 'aparcamientos.views.personalizar'),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_URL}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'aparcamientos.views.pagina_principal'),
    url(r'^login' , 'aparcamientos.views.loginuser'),
    url(r'^logout', 'aparcamientos.views.mylogout'),
    url(r'^aparcamientos/$', 'aparcamientos.views.aparcamientos'),
    url(r'^aparcamientos/(.*)', 'aparcamientos.views.aparcamientos_id'),
    url(r'^about/', 'aparcamientos.views.about'),
    url(r'^(.*)/xml/', 'aparcamientos.views.usuarios_xml'),
    url(r'^(.*)/$', 'aparcamientos.views.usuarios'),
]
