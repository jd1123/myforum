from django.conf.urls import patterns, url
from weddingpics import views

urlpatterns = patterns('',
                       url(r"^$",views.index, name = "index"),
                       url(r'^file/(?P<filename>.*)$', views.retrieve_file, name="file"),
                       #url(r'^debug/$', views.debug_hosts, name = 'debug'),
                       )
