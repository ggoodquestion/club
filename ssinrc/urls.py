from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import login ,logout ,register ,home
from text.views import about ,class1 ,declare ,index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ssinrc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^index/$', index),
    url(r'^about/$', about),
    url(r'^declare/$', declare),
    url(r'^class/$', class1),
    url(r'^accounts/register/$', register),
)
