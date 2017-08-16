from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.index),
    url(r'^news$', views.new),
    url(r'^create/(?P<nblogs>\w+)$', views.create),
    url(r'^show/(?P<bnum>\d+)$', views.show),
    url(r'^edit/(?P<enum>\d+)/edit$', views.edit),
    url(r'^delete(?P<dnum>\d+)/delete$', views.destory)
    

]