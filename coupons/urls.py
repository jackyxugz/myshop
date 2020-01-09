# -*- coding : utf-8 -*-
# coding: utf-8

from django.urls import path
from . import views

app_name = 'coupons'

urlpatterns = [
    path('apply/', views.coupon_apply, name='apply'),

]