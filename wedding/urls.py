from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^weddings/$', views.weddings, name="weddings"),
    url(r'^wedding/create/$', views.wedding_create, name='wedding_create'),
    url(r'^weddings/(?P<pk>\d+)/update$', views.wedding_update, name="wedding_update"),
    url(r'^weddings/(?P<pk>\d+)/delete$', views.wedding_delete, name="wedding_delete"),
]
