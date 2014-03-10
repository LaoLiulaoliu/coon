#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yuande Liu <miracle (at) gmail.com>

from django import forms

class registForm(forms.Form):
    email = forms.EmailField(label="邮箱", required=True, max_length=30, min_length=5)
    password = forms.CharField(label="密码", required=True, max_length=30, min_length=5, widget=forms.PasswordInput())


class loginForm(forms.Form):
    email = forms.EmailField(label="邮箱", required=True, max_length=30, min_length=5)
    password = forms.CharField(label="密码", required=True, max_length=30, min_length=5, widget=forms.PasswordInput())
