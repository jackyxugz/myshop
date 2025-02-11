#!/usr/bin/env python
# -*- coding : utf-8 -*-
# coding: utf-8

from django.urls import path
from . import views


app_name = 'payment'

urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('done/', views.payment_done, name='done'),
    path('process/', views.payment_canceled, name='canceled'),
]