from django.conf.urls import url
from . import views

app_name = 'poll';

urlpatterns = [
    #/poll/
    url(r'^$', views.index, name='index'),

    #/poll/5/
    url(r'^(?P<topic_id>[0-9]+)/$', views.detail, name='detail'),

    #/poll/5/vote/
    url(r'^(?P<topic_id>[0-9]+)/vote/$', views.vote, name='vote'),

    #/poll/5/results/
    url(r'^(?P<topic_id>[0-9]+)/results/$', views.results, name='results'),
]
