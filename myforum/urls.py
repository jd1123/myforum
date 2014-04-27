from django.conf.urls import patterns, include, url
import forum

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myforum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^forum/',include('forum.urls')),
    url(r"^$",forum.views.root, name = "root"),
)
