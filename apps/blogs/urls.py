from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^blogs/new/(?P<words>\w+)$', views.new),
    url(r'^blogs/create/(?P<nblogs>\w+)$', views.create),
    url(r'^blogs/(?P<bnum>\d+)$', views.show),
    url(r'^blogs/(?P<enum>\d+)/edit/$', views.edit),
    url(r'^blogs/(?P<dnum>\d+)/delete/$', views.destory),
    

]