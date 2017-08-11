from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^(?P<feed>\w+)/$', views.index, name='feed'),
]
