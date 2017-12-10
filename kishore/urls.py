from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^submit$', views.submit, name='ksubmit'),
    url(r'^viewresponses$', views.responselist, name='kgetresponses'),
    url(r'^viewresponse$', views.viewresponse, name = 'kviewresponse')
    ]
