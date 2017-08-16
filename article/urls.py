from django.conf.urls import url, include
from article import views

urlpatterns = [
    url(r'^myview/$', views.myview),
    url(r'^hello_world/$', views.hello_world),
    url(r'^nama_saya/(?P<nama_saya>[\w-]+)/(?P<umur>[0-9]+)$', views.nama),
]