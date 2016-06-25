from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new/$', views.contact_new, name='contact_new'),
]
