from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^(?P<nblogs>\w+)$', views.create),
    url(r'^(?P<bnum>\d+)$', views.show),
    url(r'^(?P<enum>\d+)/edit$', views.edit),
    url(r'^(?P<dnum>\d+)/delete$', views.destory)
    

]