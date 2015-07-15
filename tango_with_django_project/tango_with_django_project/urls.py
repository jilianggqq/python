#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
# At the top of your urls.py file, add the following line:
from django.conf import settings
from django.conf.urls import patterns
# from rango import views
# import rango
import logging
logging.basicConfig(level=logging.DEBUG)

urlpatterns = [
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),  # ADD THIS NEW TUPLE!
    # url(r'^media/(?P<path>.*)', 'serve', "{'document_root': settings.MEDIA_ROOT}"),
    # url(r'^rango/', rango.views.index), # ADD THIS NEW TUPLE!
]
# logging.debug("urlpatterns:" + urlpatterns)
print urlpatterns
# UNDERNEATH your urlpatterns definition, add the following two lines:
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
         'serve',
         {'document_root': settings.MEDIA_ROOT}), )

logging.debug("*********************urls.py loaded*****************")
