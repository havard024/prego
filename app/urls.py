__author__ = 'havard'

from django.conf.urls.defaults import patterns, url

from app.views import IndexView

urlpatterns = patterns('',
    url(r'^/$', IndexView.as_view()))