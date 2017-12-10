from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^submit$', views.submit, name='asubmit'),
    url(r'^viewresponses$', views.responselist, name='agetresponses'),
    url(r'^viewresponse$', views.viewresponse, name = 'aviewresponse')
    ]
