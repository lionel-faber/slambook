from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^submit$', views.submit, name='submit'),
    url(r'^viewresponses$', views.responselist, name='getresponses'),
    url(r'^viewresponse$', views.viewresponse, name = 'viewresponse')
    ]
