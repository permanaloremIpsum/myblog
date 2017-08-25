from django.conf.urls import url, include
from article import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^myview/$', views.myview),
    url(r'^hello_world/$', views.hello_world),
    url(r'^nama_saya/(?P<nama_saya>[\w-]+)/(?P<umur>[0-9]+)$', views.nama),
    url(r'^category/$', views.cat),
    url(r'^category/(?P<id>[0-9]+)$', views.list_cat),
    url(r'^(?P<slug>[\w-]+)$', views.single),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)