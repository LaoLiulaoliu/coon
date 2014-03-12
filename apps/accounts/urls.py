#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yuande Liu <miracle (at) gmail.com>

from django.conf.urls import patterns, url

urlpatterns = patterns('apps',

    ('^regist/$', 'accounts.views.regist'),
    ('^login/$', 'accounts.views.login'),
#    ('^logout/$', 'accounts.views.logout'),
#    (r'^active/(\d{1,10})/(.*)/$', 'accounts.views.active'),
#
#    ('^login/sina/$', 'accounts.sina.index'),
#    (r'login/sina/callback/$', 'accounts.sina.callback'),
#
#    ('^login/douban/$', 'accounts.douban.index'),
#    (r'login/douban/callback/$', 'accounts.douban.callback'),
)
