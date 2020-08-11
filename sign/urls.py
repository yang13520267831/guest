# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/10 21:05
# @Author : yangpengfei
# @File : urls.py
# @Software: PyCharm


from django.conf.urls import url
from sign import views_if

app_name='sign'
urlpatterns = [
    # ex:/api/add_event/

    url(r'^add_event/', views_if.add_event, name='add_event'),
]
