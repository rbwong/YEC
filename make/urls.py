from django.conf.urls import patterns, include, url
from django.conf.urls import url

from forms import  MakeUser1Form, MakeUser2Form, MakeAppForm
from views import IndexView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', IndexView.as_view([MakeUser1Form, MakeUser2Form, MakeAppForm]), name='index_page'),
                       )
