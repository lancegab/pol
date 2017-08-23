from django.conf.urls import url
from . import views

app_name = 'poll';

urlpatterns = [
    #/poll/
    url(r'^$', views.index, name='index'),
]
