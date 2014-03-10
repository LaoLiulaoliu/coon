#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yuande Liu <miracle (at) gmail.com>

from django.conf.urls import patterns, url
from critique import views

urlpatterns = patterns('',

    url(r'^(?P<company_id>\d+)', views.company, name='company'),
    url(r'^edit/(?P<company_id>\d+)', views.coedit, name='coedit'),
    url(r'^pop/(?P<company_id>\d+)/(?P<user_id>\d+)$', views.pop, name='pop'),
)
