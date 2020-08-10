# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/10 21:06
# @Author : yangpengfei
# @File : views_if.py
# @Software: PyCharm


from django.http import JsonResponse
from sign.models import Event
from django.core.exceptions import ValidationError

# 添加发布会接口
