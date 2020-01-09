# -*- coding : utf-8 -*-
# coding: utf-8

from django.db import models
from django.core.validators import MinValueValidator, \
    MaxValueValidator


class Coupon(models.Model):
    code = models.CharField(max_length=50,
                            unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(100)])
    active = models.BooleanField()

    def __str__(self):
        return self.code

    class Meta:
        ordering = ('-valid_from',)
        verbose_name = '优惠劵'
        verbose_name_plural = '优惠券'

